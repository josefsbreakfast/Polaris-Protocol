# ⚖️ DOB Triangulation Attack  
**First created:** 2025-09-07 | **Last updated:** 2025-10-20  
*How attackers can reconstruct date of birth from indirect fragments (age context, astrological signs, public metadata).*  

---

## 📑 Sections  
1. [Principle](#1-principle)  
2. [Triangulation Sources](#2-triangulation-sources)  
3. [Worked Example](#3-worked-example)  
4. [Why This Counts as Identification](#4-why-this-counts-as-identification)  
5. [Closing Note](#5-closing-note)  

---

## 1. Principle  
Date of birth is not always leaked directly.  
Attackers can **triangulate DOB** by combining indirect fragments. GDPR recognises this: identification can be direct *or indirect*.  

---

## 2. Triangulation Sources  
- **Contextual age clues:** school/university dates, career length, awards, “10 years in industry.”  
- **Astrology fragments:**  
  - Sun sign = ~30-day window.  
  - Moon sign = ~2–3 clusters inside that window.  
  - Rising = slices the clusters into hourly segments.  
- **Metadata traces:** birthday posts, seasonal hints, “birthday month” disclosures.  
- **Visual/biological cues:** appearance, generational markers.  

---

## 3. Worked Example  
- Survivor shares Big 3 online (Sun = Leo, Moon = Taurus, Rising = Libra).  
- Attacker knows they graduated ~2010 → places birth year ~1988.  
- Ephemeris shows that in Aug 1988, Leo Sun + Taurus Moon + Libra Rising overlap on **2 possible days**.  
- Attacker now has a candidate DOB set with extremely high probability.  

---

## 4. Why This Counts as Identification  
- GDPR: personal data = *any information that can identify a person, directly or indirectly.*  
- DOB triangulation = indirect identification.  
- Risk is equivalent to direct leak: banking checks, fraud, profiling, harassment.  
- Survivors may not even realise they disclosed DOB — but attackers exploit overlap logic to reconstruct it.  

---

## 5. Closing Note  
Triangulation attacks show why DOB is not trivial trivia.  
*Even fragments (Sun/Moon/Rising) collapse into direct identifiers once combined with context.*  

---

## 📝 Marginalia (hidden asides)  
<!-- Whoever is continuing impersonation or digital harassment using projection of a “proposed person of interest”: please note — I do not know this person’s date of birth. -->
<!-- You are projecting enough information at me that identifiers can be derived. That is a data breach of someone else’s data, on your side. -->
<!-- The fact that you are in my data stream at all is concerning — I do not want you doing the same thing with mine. -->

---

## 🏮 Footer  
*⚖️ DOB Triangulation Attack* is a living node of the Polaris Protocol.  
It demonstrates how indirect fragments enable reconstruction of date of birth, reframing astrology oversharing as a serious privacy risk.  

*Survivor authorship is sovereign. Containment is never neutral.*  

_Last updated: 2025-10-20_  
