[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18084390.svg)](https://doi.org/10.5281/zenodo.18084390)
# Can Infinity Collapse to Zero?
### Interpreting Real Numbers Through Infinite-Digit Representations on the Real Number Line

This project explores a universal representation format for real numbers
using *infinite digits to both the left and right* of the decimal point.

Traditional real numbers allow infinite expansion only on the **right**
(irrational decimals), while the **left** side must remain finite.
However, by extending the left side infinitely — similar to p-adic 
number systems — new mathematical behaviors emerge.

---

## 🔍 Core Idea

We represent any real number in the form:

... d₃ d₂ d₁ d₀ . d'₀ d'₁ d'₂ d'₃ ...
where
dn is a digit at nth position left to decimal (index starts at 0)
d'n is a digit at nth position right to decimal (index starts at 0)

This representation allows:

- **Right-infinite digits** → irrational expansions  
- **Left-infinite digits** → p-adic-style expansions  
- **A unified infinite-digit format** that can, in principle, express any real number  

Examples:


1  = ... 0 0 0 1 . 0 0 0 ...
π  = ... 0 0 0 3 . 1 4 1 5 9 ...

---

## 🧩 Constructing the “Largest Possible Number”

If every digit (left and right) is filled with the largest digit (9):


... 9 9 9 9 9 . 9 9 9 9 9 ...

This number naturally splits into two parts:

### **Left side**

... 9 9 9 9 9 .
In **10-adic arithmetic**, this equals **–1**.

### **Right side**

. 9 9 9 9 9 ...
In **real arithmetic**, this equals **1**.

Thus, the combined “largest possible number” becomes:


(-1) + (1) = 0

This leads to the core question:

### **👉 Can the attempt to represent infinity actually collapse to zero?**

---

## 📘 Contents

- `/paper/outline.md` – conceptual outline of the idea  
- `/examples/` – demonstrations and numeric illustrations  
- `/figures/` – diagrams for number representations  

A formal LaTeX paper will be added soon.

---

## 📌 Goals of This Project

- Explore infinite-digit positional systems  
- Connect real and p-adic number interpretations  
- Examine how “infinity” and “zero” can appear equivalent in this framework  
- Show that negative real numbers can be expressed **without writing the minus sign**  
- Provide intuitive explanations, proofs, and diagrams  

---

## TIP

for simpler and visual understanding see figures folder

## 🤝 Contributions

Feel free to open issues or pull requests to extend, challenge, or refine the ideas.

---

## 📄 License

MIT License
