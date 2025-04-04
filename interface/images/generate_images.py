
import matplotlib.pyplot as plt

plt.text(0.5, 0.5, r'$A_n^k = \frac{n!}{(n-k)!}$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/1.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

plt.text(0.5, 0.5, r'$\overline{A}_n^k = n^k$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/2.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

plt.text(0.5, 0.5, r'$P_n = n!$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/3.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

plt.text(0.5, 0.5, r'$P_n (n_1, n_2, \ldots, n_k) = \frac{n!}{n_1! n_2 ! \ldots n_k!}$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/4.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

plt.text(0.5, 0.5, r'$C_n^k = \frac{n!}{k! (n-k)!}$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/5.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

plt.text(0.5, 0.5, r'$\overline{C}_n^k = C_{n+k-1}^k$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/6.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

plt.text(0.5, 0.5, r'$P(A) = \frac{C^k_m}{C^k_n}$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/7.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()

plt.text(0.5, 0.5, r'$P(A) = \frac{C^k_m * C^{k-r}_{n-m}}{C^{k}_{n}}$', fontsize=24, ha='center', va='center')
plt.axis("off")
plt.savefig("interface/images/8.png", bbox_inches='tight', pad_inches=0.1, dpi=100)
plt.close()


