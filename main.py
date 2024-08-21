from CloudPointGridCutting import CloudPointGridCutting
import open3d as o3d

if __name__ == '__main__':
    point_cloud = o3d.io.read_point_cloud("data/bunny.ply")
    x_block = 4
    y_block = 4
    cloud_point_grid_cutting = CloudPointGridCutting(x_block, y_block, point_cloud, 'output')
    blocks = cloud_point_grid_cutting.grid_cutting()
    cloud_point_grid_cutting.output_files()