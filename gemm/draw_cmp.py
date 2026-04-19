import numpy as np
import matplotlib.pyplot as plt

# 读取 CSV 文件（跳过表头）
data1 = np.genfromtxt('/workspace/cuda_code/course5_1/sgemm_benchmark_v1.csv', delimiter=',', skip_header=1)
data2 = np.genfromtxt('/workspace/cuda_code/course5_1/sgemm_benchmark_v2.csv', delimiter=',', skip_header=1)

# 提取三列数据
sizes = data1[:, 0]          # Size
mygemm1_time = data1[:, 2]    # MySGEMM_v1_Time_ms
mygemm2_time = data2[:, 2]    # MySGEMM_v1_Time_ms
print(mygemm1_time)
print(mygemm2_time)
ratio =  mygemm2_time / mygemm1_time /1.
print(ratio)
# 创建图表
plt.figure(figsize=(10, 6))

# 绘图
plt.plot(sizes, mygemm1_time, label="mygemm1 GFLOPS", marker='o', color='blue')
plt.plot(sizes, mygemm2_time, label="mygemm2 GFLOPS", marker='s', color='orange')

# 设置图表标题和坐标轴标签
plt.title("MySGEMM_v1 vs MySGEMM_v2 GFLOPS", fontsize=14)
plt.xlabel("Matrix Size (N x N)", fontsize=12)
plt.ylabel("GFLOPS", fontsize=12)

# 设置 y 轴为对数刻度
# plt.yscale('log')

# 图例
plt.legend()

# 网格
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 自动调整布局
plt.tight_layout()

# 保存图像到文件（可选）
plt.savefig("mysgemm_v1_vs_mysgemm_v2_comp.png", dpi=300)

# 显示图表
plt.show()
