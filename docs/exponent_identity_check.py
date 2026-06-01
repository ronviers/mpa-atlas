"""
Three-way s-exponent identity check (closed-form adjudication).

MPA engine claim (character_receipts_engine.md S9, boxed):
    alpha_s = beta_mem = anomalous heavy-traffic exponent
under the "common-exponent condition" (memory kernel and load-arrival
process share one anomalous-diffusion exponent).

This script does NOT simulate. It evaluates the three legs as the
literature closed forms the framework cites, parametrized by ONE shared
anomalous-diffusion exponent beta in (0,1] (beta=1 = Markovian):

  Leg 1  (Pottier non-Markovian FDR + Caputo memory kernel):
         alpha_s = beta_mem = beta            -- linear, the diagonal.

  Leg 2a (Norros fBm-queue heavy traffic, pa:fbm-queueing):
         <Q> ~ (1-rho)^(-H/(1-H)),  H = beta/2 (subdiffusion <x^2>~t^beta)
         => exponent = beta / (2 - beta).

  Leg 2b (M/G/1 heavy-tailed service, pa:kingman tail-index alpha=1+beta):
         W ~ (1-rho)^(-1/(alpha-1))  => exponent = 1/beta.

If the three are "the same number" the curves must coincide. They meet
ONLY at beta=1 (Markovian). The point of the figure is to show that the
literal numerical identity is a Markovian-only coincidence, and that the
surviving predictive content is the TRANSPORT MAP between registers.
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

import numpy as np
import matplotlib.pyplot as plt

beta = np.linspace(0.02, 1.0, 400)

leg1_memory   = beta                 # alpha_s = beta_mem  (Pottier/Caputo)
leg2_norros   = beta / (2.0 - beta)  # fBm queue, H = beta/2  (Norros)
leg2_mg1      = 1.0 / beta           # M/G/1 heavy-tailed service (Kingman tail)

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(beta, leg1_memory, lw=3.2, color="#1f6feb",
        label=r"Leg 1  $\alpha_s=\beta_{mem}=\beta$   (FDR aging / memory kernel)")
ax.plot(beta, leg2_norros, lw=3.2, color="#d1242f",
        label=r"Leg 2a  $\beta/(2-\beta)$   (Norros fBm queue, heavy traffic)")
ax.plot(beta, leg2_mg1, lw=3.2, color="#1a7f37",
        label=r"Leg 2b  $1/\beta$   (M/G/1 heavy-tailed service)")

# Markovian coincidence point
ax.plot([1.0], [1.0], "o", ms=14, color="black", zorder=5)
ax.annotate("Markovian point\n(the ONLY place all three coincide)",
            xy=(1.0, 1.0), xytext=(0.55, 1.55),
            fontsize=13, ha="center",
            arrowprops=dict(arrowstyle="->", lw=1.8))

# shade the non-Markovian band where they diverge
ax.axvspan(0.02, 0.98, color="0.93", zorder=0)
ax.text(0.62, 0.42, "non-Markovian:\nthree DIFFERENT numbers",
        fontsize=14, ha="center", color="0.25")

ax.set_xlim(0, 1.05)
ax.set_ylim(0, 3.2)
ax.set_xlabel(r"shared anomalous-diffusion exponent  $\beta$   ($\beta=1$ Markovian)",
              fontsize=14)
ax.set_ylabel("measured exponent in each register", fontsize=14)
ax.set_title("MPA three-way s-exponent 'identity': literal equality is Markovian-only\n"
             "(the legs are different functions of one underlying exponent)",
             fontsize=15)
ax.legend(fontsize=12, loc="upper left", framealpha=0.95)
ax.grid(alpha=0.3)

out = "H:/mpa-atlas/docs/exponent_identity_check.png"
fig.savefig(out, dpi=300, bbox_inches="tight")
print("wrote", out)

# print the gap at a few operating points
print("\nbeta   memory   Norros   M/G/1   (all equal only at beta=1)")
for b in [1.0, 0.8, 0.6, 0.4, 0.2]:
    print(f"{b:4.2f}   {b:6.3f}   {b/(2-b):6.3f}   {1.0/b:6.3f}")
