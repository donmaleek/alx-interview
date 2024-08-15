#!/usr/bin/python3
""" Rotate 2D Matrix"""


def rotate_2d_matrix(mat):
    """Rotates 2d mat by 90 degrees"""
    N = len(mat[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = mat[i][j]
            mat[i][j] = mat[N - 1 - j][i]
            mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
            mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
            mat[j][N - 1 - i] = temp
