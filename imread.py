import cv2 as cv
import numpy as np


def add_demo(m1,m2):#像素的加运算
    dst =cv.add(m1,m2)
    cv.imshow("add_demo",dst)


def subtract_demo(m1,m2):#像素的减运算
    dst =cv.subtract(m1,m2)
    cv.imshow('subtract_demo',dst)


def divide_demo(m1,m2):#像素的除法运算
    dst =cv.divide(m1,m2)
    cv.imshow('divide_demo',dst)


def multiply_demo(m1,m2):#像素的乘法运算
    dst =cv.multiply(m1,m2)
    cv.imshow('multiply_demo',dst)


src1 =cv.imread('e:/morph01.png')
src2 =cv.imread('e:/morph01.png')
add_demo(src1,src2)
subtract_demo(src1,src2)
divide_demo(src1,src2)
multiply_demo(src1,src2)
cv.waitKey(0)
