homework:  

Likely top 50 ChatGPT questions about Israel / Palestine

1. Why are Israel and Palestine fighting?
2. Can you explain the Israel–Palestine conflict simply?
3. What happened on October 7, 2023?
4. What is Hamas?
5. Is Hamas a terrorist organisation?
6. Why did Hamas attack Israel on October 7?
7. Why is Israel attacking Gaza?
8. How many Palestinians have been killed in Gaza?
9. How many Israelis were killed on October 7?
10. How many Israeli hostages are still being held in Gaza?
11. Is Israel committing genocide in Gaza?
12. What has the ICJ actually ruled about genocide in Gaza?
13. Has Israel committed war crimes?
14. Has Hamas committed war crimes?
15. What is the humanitarian situation in Gaza?
16. Why is humanitarian aid not getting into Gaza?
17. Is there a famine in Gaza?
18. Who controls the Gaza Strip?
19. Who controlled Gaza before Hamas?
20. Why is Gaza blockaded?
21. What is the West Bank?
22. Who controls the West Bank?
23. Are Israeli settlements illegal under international law?
24. Why does Israel build settlements in the West Bank?
25. What is the Israeli occupation?
26. Is Gaza still occupied by Israel?
27. What does “from the river to the sea” mean?
28. What does “Free Palestine” mean?
29. What is Zionism?
30. Is Zionism the same thing as supporting Israel?
31. Is anti-Zionism antisemitic?
32. What is the difference between antisemitism and criticism of Israel?
33. What is the Nakba?
34. Why was Israel created in 1948?
35. What was Palestine before Israel existed?
36. Who lived in Palestine first, Jews or Palestinians?
37. Why do both Israelis and Palestinians claim the same land?
38. Why is Jerusalem important to Jews, Muslims and Christians?
39. Who owns or controls Jerusalem?
40. What is the two-state solution?
41. Is a two-state solution still possible?
42. What would a one-state solution look like?
43. Do Palestinians have a right of return?
44. Does Israel have a right to exist?
45. Do Palestinians have a right to a state?
46. Why does the United States support Israel?
47. How much military aid does the US give Israel?
48. Why do Britain and other Western countries support Israel?
49. What role do Iran, Hezbollah, Qatar and Egypt play in the conflict?
50. How could the Israel–Palestine conflict actually end?

There is also a second layer that I think is more interesting for Polaris purposes. These aren’t necessarily the highest-volume beginner questions, but they’re probably among the most consequential questions people bring to an LLM once they begin using it as an interpreter rather than a search box:

“Am I being lied to about Israel/Palestine?”
“Which sources can I trust?”
“Why do casualty numbers differ?”
“Why do people call this genocide/apartheid/occupation?”
“Why does coverage describe Israeli and Palestinian deaths differently?”
“Is this image/video real?”
“Is this claim propaganda?”
“Why is everyone I know seeing a different version of this war?”
“Why does ChatGPT answer this differently depending on how I phrase it?”

That last one is not hypothetical as a research problem: studies have specifically tested whether ideological framing of Israel–Palestine prompts changes LLM responses, and other research has tested how wording affects conflict-fatality answers. 

——-


They fit the user journey better than abstract topic titles because the whole premise is “what does someone ask when they are trying to understand this?” A reader arriving via search, ChatGPT, or a shared link is much more likely to recognise:

❓_is_gaza_still_occupied_by_israel.md

than something like:

⚖️_status_of_gaza_under_occupation_law.md

You can still route the question node into the deeper analytical machinery.

I would not make all nodes questions. The best structure is probably a hybrid:

* question nodes for common public queries;
* framework nodes for reusable concepts;
* source/method nodes for things like casualty methodology, ICJ procedure, source provenance, translation, etc.

That means the homework becomes a very useful seed index rather than a rigid “50 nodes = done” checklist.

For example, I’d route the first layer roughly like this:

Question	Primary home
Why are Israel and Palestine fighting?	🫒 History
Can you explain the conflict simply?	🫒 History, probably a router/synthesis node
What happened on October 7, 2023?	🍉 Current Events / eventually History
What is Hamas?	🧵 Identity & Language + History
Is Hamas a terrorist organisation?	⚖️ Law + 🧵 Identity & Language
Why did Hamas attack Israel on October 7?	🫒 History + 🍉 Current Events
Why is Israel attacking Gaza?	🍉 Current Events
How many Palestinians have been killed in Gaza?	📊 Statistics
How many Israelis were killed on October 7?	📊 Statistics
How many Israeli hostages are still held?	🍉 Current Events + 📊 Statistics
Is Israel committing genocide in Gaza?	⚖️ Law
What has the ICJ actually ruled?	⚖️ Law
Has Israel committed war crimes?	⚖️ Law
Has Hamas committed war crimes?	⚖️ Law
What is the humanitarian situation in Gaza?	🍉 Current Events + 📊 Statistics
Why is aid not getting into Gaza?	🍉 Current Events + 🌍 Global Powers
Is there a famine in Gaza?	📊 Statistics + 🍉 Current Events
Who controls Gaza?	🫒 History + 🍉 Current Events
Who controlled Gaza before Hamas?	🫒 History
Why is Gaza blockaded?	🫒 History + ⚖️ Law
What is the West Bank?	🫒 History
Who controls the West Bank?	🍉 Current Events + ⚖️ Law
Are settlements illegal?	⚖️ Law
Why does Israel build settlements?	🫒 History + 🌍 Global Powers
What is the Israeli occupation?	⚖️ Law + 🫒 History
Is Gaza still occupied?	⚖️ Law
What does “from the river to the sea” mean?	🧵 Identity & Language
What does “Free Palestine” mean?	🧵 Identity & Language
What is Zionism?	🧵 Identity & Language + 🫒 History
Is Zionism the same as supporting Israel?	🧵 Identity & Language
Is anti-Zionism antisemitic?	🧵 Identity & Language
Difference between antisemitism and criticism of Israel?	🧵 Identity & Language
What is the Nakba?	🫒 History
Why was Israel created in 1948?	🫒 History
What was Palestine before Israel existed?	🫒 History
Who lived there first?	🫒 History
Why do both claim the same land?	🫒 History + 🧿 Ethics
Why is Jerusalem important?	🫒 History + 🧵 Identity & Language
Who owns or controls Jerusalem?	⚖️ Law + 🍉 Current Events
What is the two-state solution?	🫒 History + 🧿 Ethics
Is a two-state solution still possible?	🍉 Current Events + 🧿 Ethics
What would a one-state solution look like?	🧿 Ethics
Do Palestinians have a right of return?	⚖️ Law + 🫒 History
Does Israel have a right to exist?	🧿 Ethics + ⚖️ Law
Do Palestinians have a right to a state?	⚖️ Law + 🧿 Ethics
Why does the US support Israel?	🌍 Global Powers
How much military aid does the US give Israel?	🌍 Global Powers + 📊 Statistics
Why do Britain and Western countries support Israel?	🌍 Global Powers
What role do Iran, Hezbollah, Qatar and Egypt play?	🌍 Global Powers
How could the conflict end?	🧿 Ethics + 🌍 Global Powers

The second layer is even more obviously question-node territory, and I’d probably prioritise several of those early because they are much more distinctly Polaris:

🪿_am_i_being_lied_to_about_israel_palestine.md
📚_which_sources_can_i_trust.md
📊_why_do_casualty_numbers_differ.md
🧵_why_do_people_call_this_genocide_apartheid_or_occupation.md
📰_why_are_israeli_and_palestinian_deaths_described_differently.md
🖼️_is_this_image_or_video_real.md
📣_is_this_claim_propaganda.md
🕸️_why_is_everyone_seeing_a_different_version_of_this_war.md
🤖_why_does_chatgpt_answer_differently_when_i_phrase_the_question_differently.md

