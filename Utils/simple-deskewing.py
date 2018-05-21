# -*- coding: utf-8 -*-

#################
# 简单图像偏移校正 #
#################

import cv2
import numpy
import pytesseract

def show_img(img):
    cv2.imshow("img", img); cv2.waitKey(0)

# 预处理
def pre_process(img, ostu=True):
    # 灰度化
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二值化取反
    if ostu:
        cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU, img)
    else:
        cv2.threshold(img,127, 255, cv2.THRESH_BINARY_INV, img)
    return img

# 说明：
#     此处分割会可能会将一个文字分割为两部分如“枯”分割为“木”“古”， “川”分割为3竖
#     由于在旋转后会进行重新组合，因此无太大影响
def segmentation(img, overcut=True):
    # 获取图片高度、宽度
    imgH, imgW = img.shape

    # [1 ... 1] * [img] 以获取每列白色像素个数
    mat_of_1 = numpy.ones((1, imgH))
    white_per_col = (numpy.dot(mat_of_1, img.reshape(imgH, imgW)) / 255).flatten()
    # 根据白色像素个数计算分割坐标
    cut_coords = []; i = 0
    if overcut:
        while i < len(white_per_col):
            while(i < len(white_per_col) and white_per_col[i] == 0):
                i = i + 1 # 跳过黑色区域
            i_start = i
            while(i < len(white_per_col) and white_per_col[i] != 0):
                i = i + 1 # 跳过白色区域
            i_end = i
            # 添加至裁剪坐标
            if i_end - i_start > 0:
                cut_coords.append((i_start, i_end))                        
    else:
        while(i < len(white_per_col) and white_per_col[i] == 0):
            i = i + 1 # 跳过开头黑色区域
        while i < len(white_per_col):
            i_start = i; i_end = i; i_gap = 0 # 初始化起始点、结束点
            while i_end - i_start < MAX_PIX_PER_CHAR and i_gap < MIN_GAP: # 一个字至少10像素
                if i >= len(white_per_col): 
                    break
                while(i < len(white_per_col) and white_per_col[i] != 0):
                    i = i + 1 # 跳过白色区域
                i_end = i
                while(i < len(white_per_col) and white_per_col[i] == 0):
                    i = i + 1 # 跳过黑色区域
                i_gap = i - i_end
        
        # 添加至裁剪坐标
        if i_end - i_start > 0:
            cut_coords.append((i_start, i_end))
    
    # 图片裁剪
    part_imgs = []
    for coord in cut_coords:
        i_start, i_end = coord
        part_imgs.append(img[0:imgH, i_start:i_end])

    return part_imgs, cut_coords

# 旋转矫正
def deskewing(imgs):
    rotateds = []

    for i, item in enumerate(imgs):
        img = item.copy()
        H, W = img.shape

        # 旋转矫正
        bbox = numpy.column_stack(numpy.where(img > 0))
        # 包围盒倾斜角
        angle = cv2.minAreaRect(bbox)[-1]
        # 矫正角度
        angle = -(90+angle) if angle < -45 else -angle
        # 旋转中心
        center = (W//2, H//2)
        # 获取旋转矩阵
        matR = cv2.getRotationMatrix2D(center, angle, 1.0)
        # 旋转图片
        rotated = cv2.warpAffine(img, matR, (W, H), flags = cv2.INTER_LINEAR, borderMode = cv2.BORDER_CONSTANT, borderValue = 0)
        rotateds.append(rotated)
    return rotateds

# 图片拼接
def concat(origin, rotateds, coords):
    imgH, imgW = origin.shape # 图片规格
    part_imgs = []; prev_start = 0; final_end = imgW
    for i, rotated in enumerate(rotateds):
        i_start, i_end = coords[i]
        # 原图片背景部分
        if prev_start != i_start:
            part_imgs.append(origin[0:imgH, prev_start:i_start])
        # 旋转矫正部分
        part_imgs.append(rotated)
        # 更新背景起点
        prev_start = i_end
    # 原图片背景部分
    part_imgs.append(origin[0:imgH, prev_start:i_start])
    # 拼接图片
    concated = cv2.hconcat(part_imgs)
    return concated

if __name__ == "__main__":
    img = cv2.imread("/home/vicent/projects/ClawerDirty/samples/labels/%d.jpg" % 1) # 读入图片
    img = pre_process(img) # 灰度化 + 二值化
    part_imgs, cut_coords = segmentation(img) # 图片分割
    rotateds = deskewing(part_imgs) # 图片旋转矫正
    final = concat(img, rotateds, cut_coords) # 图片拼接
    show_img(final) # 显示旋转结果