import math
import string

import numpy as np
import open3d as o3d

class CloudPointGridCutting:
    def __init__(self, x_block : int, y_block : int, point_cloud: o3d.geometry.PointCloud, output_path : string = None ):
        """
        This class is used to cut the point cloud into x_block * y_block blocks
        :param x_block: number of blocks in x direction
        :param y_block: number of blocks in y direction
        :param point_cloud: input point cloud
        :param output_path: output path （default is None）
        """
        self.x_block = x_block
        self.y_block = y_block
        self.point_cloud = point_cloud
        self.output_path = output_path
        self.output = [ [] for i in range (self.y_block)]

    def grid_cutting(self):
        """
        Cut the point cloud into x_block * y_block blocks
        :return: x_block * y_block blocks
        """
        xyz = np.array(self.point_cloud.points)
        colors = np.array(self.point_cloud.colors)

        x_min = int(xyz[:, 0].min())
        x_max = math.ceil(xyz[:, 0].max())
        y_min = int(xyz[:, 1].min())
        y_max = math.ceil(xyz[:, 1].max())

        lis = [ [ [] for i in range (self.x_block)] for j in range (self.y_block)]
        x_tmp = (x_max - x_min) / self.x_block + 1
        y_tmp = (y_max - y_min) / self.y_block + 1

        for i in range(len(xyz)):
            x = int((xyz[i][0] - x_min) / x_tmp)
            y = int((xyz[i][1] - y_min) / y_tmp)
            lis[y][x].append(i)

        for i in range (self.y_block):
            for j in range (self.x_block):
                pc_tmp = o3d.geometry.PointCloud()
                pc_tmp.points = o3d.utility.Vector3dVector(xyz[lis[i][j]])
                pc_tmp.colors = o3d.utility.Vector3dVector(colors[lis[i][j]])
                self.output[i].append(pc_tmp)

        return self.output

    def output_files(self):
        """
        Output the point cloud blocks to the output path
        :return: if you did not set the output path, it will print "Output path is not set"
        """
        if self.output_path is None:
            print("Output path is not set")
            return
        for i in range (self.y_block):
            for j in range (self.x_block):
                o3d.io.write_point_cloud(self.output_path + "/output_" + str(i) + "_" + str(j) + ".ply", self.output[i][j])

    def get_x_block(self):
        return self.x_block

    def set_x_block(self, x_block : int):
        self.x_block = x_block

    def get_y_block(self):
        return self.y_block

    def set_y_block(self, y_block : int):
        self.y_block = y_block

    def get_point_cloud(self):
        return self.point_cloud

    def set_point_cloud(self, point_cloud: o3d.geometry.PointCloud):
        self.point_cloud = point_cloud

    def get_output_path(self):
        return self.output_path

    def set_output_path(self, output_path : string):
        self.output_path = output_path

    def get_output(self):
        return self.output


