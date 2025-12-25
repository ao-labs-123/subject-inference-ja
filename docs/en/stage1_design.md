Example English Template — Step 1 (Subject Resolution)

Title: Step 1 — Resolving First-Person Omitted Subjects in Dialogue AI

##　Overview:
This step focuses on improving the AI’s ability to correctly interpret sentences where the first-person subject (“I”) is omitted.
In Japanese, psychological verbs such as 思った (thought), 感じた (felt), 気づいた (noticed) strongly imply the speaker as the subject.
By codifying this linguistic pattern, the model can reduce misreadings and increase conversational accuracy.

##　Key Points:
	1.	When a psychological verb appears without a subject,
→ Assume the speaker as the subject.
	2.	If the sentence contains markers like
「〜らしい」「〜と聞いた」「〜と言われた」
→ Those imply second or third person, not the speaker.
	3.	This rule significantly reduces ambiguity in Japanese dialogue and is foundational for later stages of the system.

##　Example: 
	•	「変だと思った。」
→ The subject is the speaker.
	•	「彼が変だと思ったらしい。」
→ The subject is 彼 (he), not the speaker.
