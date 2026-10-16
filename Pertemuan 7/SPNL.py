import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

TOL, MAXIT = 1e-4, 20

# f(x) = ruas kanan - nilai y  (dicari f(x)=0)
persamaan = {
    "1) y=3x^3-5x^2+4x-7, y=1": (lambda x: 3*x**3 - 5*x**2 + 4*x - 7 - 1, (1.0, 3.0)),
    "2) y=e^x-x^2, y=0":        (lambda x: math.exp(x) - x**2,            (-1.0, 0.0)),
    "3) y=log10(x+2)+2x-3, y=0": (lambda x: math.log10(x + 2) + 2*x - 3,  (1.0, 2.0)),
}

def bisection(f, a, b, tol=TOL, maxit=MAXIT):
    """Biseksi. Berhenti jika error relatif < tol atau iterasi = maxit."""
    if f(a)*f(b) > 0: raise ValueError("f(a)*f(b) harus < 0")
    rows, c_old, konvergen = [], None, False
    for i in range(1, maxit+1):
        c = (a+b)/2
        err = abs((c-c_old)/c) if c_old is not None else None
        rows.append((i, a, b, c, f(a), f(b), f(c), err))
        if f(c) == 0 or (err is not None and err < tol):
            konvergen = True; break
        if f(a)*f(c) < 0: b = c
        else: a = c
        c_old = c
    return c, rows, konvergen

def regula_falsi(f, a, b, tol=TOL, maxit=MAXIT):
    """Regula falsi. Berhenti jika error relatif < tol atau iterasi = maxit."""
    if f(a)*f(b) > 0: raise ValueError("f(a)*f(b) harus < 0")
    rows, c_old, konvergen = [], None, False
    for i in range(1, maxit+1):
        c = b - f(b)*(b-a)/(f(b)-f(a))
        err = abs((c-c_old)/c) if c_old is not None else None
        rows.append((i, a, b, c, f(a), f(b), f(c), err))
        if f(c) == 0 or (err is not None and err < tol):
            konvergen = True; break
        if f(a)*f(c) < 0: b = c
        else: a = c
        c_old = c
    return c, rows, konvergen

def cetak(nama, rows):
    print(f"  {nama}   (error = |(c_baru - c_lama)/c_baru|)")
    print(f"  {'i':>2} {'a':>10} {'b':>10} {'c':>10} {'f(a)':>10} {'f(b)':>10} {'f(c)':>10} {'error':>10}")
    for i,a,b,c,fa,fb,fc,e in rows:
        es = "-" if e is None else f"{e:.6f}"
        print(f"  {i:>2} {a:10.6f} {b:10.6f} {c:10.6f} {fa:10.6f} {fb:10.6f} {fc:10.6f} {es:>10}")

def grafik(nama, f, interval, idx, akar):
    # Grafik tunggal: f(x) memotong sumbu x
    x = np.linspace(interval[0]-1, interval[1]+1, 400)
    y = np.array([f(v) if (v+2>0 or "log" not in nama) else np.nan for v in x])
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].plot(x, y, label="f(x)"); ax[0].axhline(0, color="k", lw=.8)
    ax[0].plot(akar, 0, "ro", label=f"akar ≈ {akar:.4f}")
    ax[0].set_title("Grafik tunggal: f(x)=0"); ax[0].grid(True); ax[0].legend()
    # Grafik ganda: pisahkan f(x)=g(x)-h(x), gambar g(x) dan h(x)
    g, h = ganda[idx]
    ax[1].plot(x, [g(v) for v in x], label="g(x)")
    ax[1].plot(x, [h(v) for v in x], label="h(x)")
    ax[1].plot(akar, g(akar), "ro")
    ax[1].set_title("Grafik ganda: g(x)=h(x)"); ax[1].grid(True); ax[1].legend()
    plt.tight_layout(); plt.savefig(f"grafik_{idx+1}.png", dpi=120); plt.close()

# pemisahan untuk grafik ganda
ganda = [
    (lambda x: 3*x**3 - 5*x**2 + 4*x - 7, lambda x: 1),
    (lambda x: math.exp(x),               lambda x: x**2),
    (lambda x: math.log10(x+2),           lambda x: 3 - 2*x),
]

for idx, (nama, (f, (a, b))) in enumerate(persamaan.items()):
    print("="*80); print(nama, f"  selang [{a}, {b}]")
    cb, rb, kb = bisection(f, a, b); cr, rr, kr = regula_falsi(f, a, b)
    st = lambda k: "error < toleransi" if k else "BERHENTI di iterasi maksimum (belum konvergen)"
    cetak("Metode Biseksi", rb);  print(f"  -> akar = {cb:.6f}, iterasi = {len(rb)}, {st(kb)}\n")
    cetak("Metode Regula Falsi", rr); print(f"  -> akar = {cr:.6f}, iterasi = {len(rr)}, {st(kr)}\n")
    grafik(nama, f, (a, b), idx, cb)