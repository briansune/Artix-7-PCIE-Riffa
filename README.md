# Artix-7-PCIE-Riffa

### This project is just an extension of previous Riffa
### As XDMA on Windows 10 and 11 are introduce all kinds of trouble

Riffa repository link: https://github.com/KastnerRG/riffa

---

### For those who are not familiar with Riffa

### Riffa is an open PCIe communication design with low-resource and easy to use.

So far Windows 10 or Linux can communicate with the Riffa driver.

Additional make or compile may involves but it is sure that basic driver setup is promising.

---

## Convert previous HDL into a IP to and make life much easier on development.

### New Method
![new_method](image/Riffa.PNG)

### Old Method
![old_method](image/old.PNG)

## Resource RIFFA PCIe x4 Gen 2.0 
| LUT    | 6343  | 63400  | 10.004732 |
|--------|-------|--------|-----------|
| LUTRAM | 202   | 19000  | 1.0631579 |
| FF     | 11759 | 126800 | 9.27366   |
| BRAM   | 43    | 135    | 31.851852 |
| IO     | 1     | 285    | 0.3508772 |
| GT     | 4     | 4      | 100.0     |
| BUFG   | 6     | 32     | 18.75     |
| MMCM   | 1     | 6      | 16.666668 |
| PCIe   | 1     | 1      | 100.0     |

---
![image](https://user-images.githubusercontent.com/29487339/172640708-8d9ebe1d-12b9-4c04-a5cc-929ddf89c2bf.png)



