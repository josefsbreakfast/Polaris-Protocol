# 🧮 Focus Group of One  
**First created:** 2025-11-17 | **Last updated:** 2025-11-17  
*How small subgroups get mathematically inflated into “the public mood” — and why one lad in Slough becomes 200,000 citizens in a policy brief.*

---

## 🛰️ Orientation  

This node explains the statistical trap behind political polling, conflict-attitude datasets, and humanitarian-opinion research:  
when a subgroup sample is tiny, **each respondent gets scaled up** to represent an entire demographic.

This is the *“Focus Group of One”* problem — the Thick of It skit made real through post-stratification weighting.

It shows up heavily in:
- conflict opinion datasets,  
- humanitarian sentiment analysis,  
- ethnographic polling slices,  
- “community voice” extracts used in ministerial briefings.

---

## ✨ Key Features  
- Clear maths explaining **why small groups get amplified**  
- Weighting formulas used in social-science datasets  
- Worked examples showing how **one person can equal 25,000**  
- Risk conditions for misinterpreting “public opinion”  
- Links to suppression theatre and narrative manufacturing  

---

## 🧿 Analysis / Content  

### 1. Why tiny subgroups get amplified  

In any cross-sectional dataset (Dartmouth, Pew, YouGov, Conflict Attitudes Index), you **never** get proportional numbers for every demographic.

If Group X is:
- **5%** of the actual population  
but only  
- **2%** of your sample  

then statistically the dataset must “correct” this by **up-weighting** each member of Group X so they reflect their true share.

This is called **post-stratification weighting**.

---

### 2. The weighting maths (simple form)

Let:

- \( N_p \) = true proportion of group in population  
- \( N_s \) = proportion of group in sample  

Then the **weight applied to each respondent** is:

\[
w = \frac{N_p}{N_s}
\]

If the population is 5% and the sample is 2%, the weight is:

\[
w = \frac{0.05}{0.02} = 2.5
\]

Every answer from that group is multiplied by 2.5.

This is fine for medium-size groups.

It becomes a nightmare for tiny groups.

---

### 3. When n is tiny, one person = tens of thousands  

Let the *absolute number* in your sample for a group be \( n \).

If the group should represent \( P \) people in the population, then each respondent represents:

\[
R = \frac{P}{n}
\]

**Worked example:**

- A minority group makes up 200,000 people nationally  
- Your survey randomly captures **8** of them

Then:

\[
R = \frac{200,000}{8} = 25,000
\]

One respondent = **25,000 inferred people**.

If one guy strongly opposes a ceasefire because he was in a mood that day, the dataset concludes:  
**“25,000 people are strongly opposed to a ceasefire.”**

Welcome to the *Focus Group of One*.

---

### 4. Volatility: why small groups behave like noise generators  

When sample size is small, variance explodes.

The **effective margin of error** for a subgroup is approximately:

\[
\text{MoE} \approx \frac{1}{\sqrt{n}}
\]

So:

- \( n = 100 \) → MoE ≈ 10%  
- \( n = 25 \) → MoE ≈ 20%  
- \( n = 9 \) → MoE ≈ 33%  
- \( n = 4 \) → MoE ≈ 50%  

Meaning:  
A 50/50 split from \( n=4 \) tells you **nothing at all**, but policy briefings often treat it as gospel.

---

### 5. How this distorts conflict & humanitarian datasets  

Small-subgroup inflation can create:

- **False polarisation**  
- **Invented “community divisions”**  
- **Overstated hostility**  
- **Understated support for humanitarian norms**  
- **Ghost trends driven by one charismatic or unhinged respondent**  
- “X group overwhelmingly supports Y extremist position” (based on n=6)

In conflict research, this is especially dangerous because:
- emotions run high,  
- demographic representation is uneven,  
- minority groups may be oversampled or undersampled.

The distortion can spill into:
- policy recommendations  
- media headlines  
- diplomatic briefs  
- humanitarian funding priorities  

---

### 6. Thick of It register — the satire made real  

This is where the admin becomes comedy.

Minister:  
> “What do young British Palestinians think about hostages and humanitarian corridors?”  

Analyst, sweating:  
> “Well, Minister, according to our dataset, 25,000 of them are *furious about bin collections*, because one respondent misclicked.”

Civil servant:  
> “So that’s… policy-relevant?”  

Weighting algorithm:  
> “Yes. Very.”  

This is what happens when mathematical necessity meets political illiteracy.

---

### 7. Real safeguards (when done properly)  

To avoid the **one person = everyone** trap, researchers should:  

- publish **subgroup sample sizes**  
- suppress or grey-out subgroups with \( n < 30 \)  
- include **design effect corrections**  
- use **MRP (multilevel regression & post-stratification)**  
- attach transparent error bars  
- refuse policy requests for “community breakdowns” when data cannot support them  

Too often, none of these safeguards are used — and the public’s “voice” becomes a statistical hallucination.

---

## 🌌 Constellations  
🧮 🧿 🛰️ ✂️ — diagnostic register; distortion-maths; narrative manufacture through data structure.

---

## ✨ Stardust  
post-stratification, sampling bias, weighting, subgroup volatility, conflict datasets, public opinion modelling, narrative distortion, political polling, humanitarian research, statistical ethics

---

## 🏮 Footer  

*🧮 Focus Group of One* is a living node of the **Polaris Protocol**.  
It documents how statistical weighting in small samples can fabricate or distort “public opinion”, especially in conflict and humanitarian research — making one respondent speak as thousands.

> 📡 Cross-references:  
> - [📿 Vulnerable Data Populations](../Metadata_Sabotage_Network/🔥_Data_Risks/📿_vulnerable_data_populations.md) — *how groups become statistically fragile*  
> - [📚 Narrative Management](../Big_Picture_Protocols/🌀_Systems_&_Governance/📚_Narrative_Management/) — *how distorted data becomes story*  
> - [🍄 Suppression Layers](../Metadata_Sabotage_Network/🍄_Suppression_Layers/) — *how weighting effects can be exploited*

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-11-17_
