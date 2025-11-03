# 🧮 k-Anonymity: Data Integrity & Re-identification Risk  

**First created:** 2025-11-02 | **Last updated:** 2025-11-02  
*A minimal guide to calculating and maintaining the k-anonymity constant in structured datasets.*

---

## 🧭 Orientation  

k-anonymity protects against re-identification by ensuring that each record in a dataset is indistinguishable from at least **k − 1** others on its quasi-identifiers (e.g., age, postcode prefix, gender).  
When data are updated or cross-linked, effective anonymity can degrade, so k must be re-evaluated over time.

---

## 🧩 Worked Example  

| Record ID | Age Range | Postcode Prefix | Gender | k-Group | Count in Group |
|------------|------------|----------------|---------|----------|----------------|
| 001 | 30–34 | SW1 | F | A | 8 |
| 002 | 30–34 | SW1 | F | A | 8 |
| … | … | … | … | … | … |
| 008 | 30–34 | SW1 | F | A | 8 |
| 009 | 45–49 | N1 | M | B | 12 |

The dataset’s **k** is the *smallest* group size → here **k = 8**.  
Every record is therefore hidden among at least 7 others that share the same quasi-identifier pattern.

---

## ⚙️  Pseudocode  

```python
# df = DataFrame containing quasi-identifiers
def k_anonymity(df, quasi_identifiers):
    groups = df.groupby(quasi_identifiers)
    group_sizes = groups.size()
    k = group_sizes.min()
    return k
```

```python
if k < policy_threshold:
    print("⚠️  Re-identification risk too high: generalise or suppress.")
else:
    print("✅  Sufficient anonymity at current granularity.")
```

---

## 🧾  If k Is Too Small  

- **Generalisation:** widen value ranges (Age → Age band).  
- **Suppression:** remove rare combinations.  
- **Noise Injection:** add statistical fuzz.  
- **Aggregation:** publish summaries, not rows.

---

## 🌌  Constellations  

🧮 📊 ⚖️ 🧾 — privacy · verification · integrity · governance  

---

## ✨ Stardust  

data privacy, k-anonymity, re-identification risk, statistical disclosure control, data integrity  

---

## 🏮 Footer  

*🧮 k-Anonymity: Data Integrity & Re-identification Risk* is a technical appendix of the Polaris Protocol.  
It outlines how to calculate the k constant and maintain anonymity as datasets evolve.  

> 📡 Cross-references:  
> - [⚖️ Threats and Countermeasures to Democracy from Machine Learning](../📊_Machine_Learning_And_Democracy/⚖️_threats_and_countermeasures_to_democracy_from_machine_learning.md) — policy context  
> - [🧭 Data Integrity and Re-identification Risk](../🧭_data_integrity_and_reidentification_risk.md) — governance overview  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-11-02_
