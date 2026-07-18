"""
legalist/data.py
───────────────
Static demo-case data and agent styling constants.
Pulled out of server.py so the server layer stays thin.
"""

# ── Agent display config ─────────────────────────────────────────────────────
AGENT_STYLE: dict[str, tuple[str, str]] = {
    "Bailiff": ("BL", "av-system"),
    "Judge": ("JD", "av-judge"),
    "Prosecutor": ("PR", "av-prosecutor"),
    "Defense": ("DF", "av-defense"),
    "Witness": ("WS", "av-witness"),
    "Magistrate": ("MG", "av-magistrate"),
    "Foreperson": ("FP", "av-foreperson"),
    "Juror": ("JR", "av-juror"),
    "Fact Checker": ("FC", "av-checker"),
    "System": ("—", "av-system"),
}

AGENT_NAME_COLOR: dict[str, str] = {
    "Judge": "#ff9f0a",
    "Prosecutor": "#ff453a",
    "Defense": "#0a84ff",
    "Defense Counsel": "#0a84ff",
    "Witness": "#30d158",
    "Foreperson": "#bf5af2",
    "Juror": "#5ac8fa",
    "Fact Checker": "#ff6961",
    "Magistrate": "#ff9f0a",
    "Bailiff": "#c9a84c",
    "System": "#48484a",
}

# ── Demo trial scripts ────────────────────────────────────────────────────────
DEMO_CASES: dict[str, dict] = {
    "ransomware": {
        "title": "State v. Dmitri Volkov — Ransomware Attack on St. Jude's Hospital",
        "jurisdiction": "United States · Federal District Court, Southern District",
        "description": (
            "The defendant, Dmitri Volkov, is charged with one count of computer intrusion "
            "(18 U.S.C. § 1030) and one count of attempted extortion related to the July 12th "
            "ransomware attack on St. Jude's Medical Center. The attack encrypted 14,000 patient "
            "records and demanded $4.2 million in Bitcoin. FBI digital forensics traced the "
            "ransomware deployment to a laptop registered to Volkov, with his SSH keys found in "
            "the system's authorized_keys file. Volkov claims he was attending the DevSecOps "
            "conference in Berlin at the time of the attack — he has passport stamps, conference "
            "badge scans, and hotel key card records placing him there. Defense argues the laptop "
            "was infected with a remote access trojan (RAT) months prior and his SSH keys could "
            "have been harvested without his knowledge."
        ),
        "questions": [
            "Could Volkov's SSH keys have been copied from his laptop without his knowledge?",
            "Does the Berlin hotel WiFi logs show continuous device activity during the attack window?",
            "Was Volkov's laptop encrypted or password-protected, and who else had physical access?",
            "Can IP geolocation evidence definitively rule out a VPN relay from Berlin to a US server?",
            "Were any other suspects identified with access to St. Jude's network infrastructure?",
        ],
        "trial_script": [
            # ════════════════ PHASE 1: DISCOVERY ════════════════
            {
                "agent": "Bailiff",
                "text": "All rise. The Honorable Justice Park presiding. The court is now in session for the Discovery Disclosure phase.",
                "phase": "Discovery",
            },
            {
                "agent": "Judge",
                "text": "Be seated. State versus Dmitri Volkov — computer intrusion and attempted extortion. The court proceeds with discovery disclosure. Mr. Mercer.",
                "phase": "Discovery",
            },
            {
                "agent": "Prosecutor",
                "text": "The People disclose: (1) Laptop seized from Volkov, Dell XPS 15, containing SSH private keys matching the authorized_keys on the compromised hospital server; (2) FBI digital forensics report by Special Agent Chen; (3) IP address logs from St. Jude's showing the intrusion originating from a VPN endpoint; (4) Blockchain transaction records linking the ransom wallet to an exchange account registered to Volkov.",
                "phase": "Discovery",
            },
            {
                "agent": "Defense",
                "text": "The defense discloses: (1) Passport showing Volkov entered Germany on July 10th and departed July 14th; (2) Hotel InterContinental Berlin key card records dated July 11-13; (3) DevSecOps Berlin conference badge scan logs placing Volkov at the venue during the attack window; (4) Expert report by Dr. Amina Patel, cybersecurity researcher, documenting a known RAT vulnerability in Volkov's laptop model that allows credential harvesting.",
                "phase": "Discovery",
            },
            {"agent": "Judge", "text": "Disclosure is complete. The court notes competing narratives on digital forensics. Proceed to pre-trial motions.", "phase": "Discovery"},
            # ════════════════ PHASE 2: PRE-TRIAL MOTIONS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to pre-trial motions.", "phase": "Motions"},
            {
                "agent": "Judge",
                "text": "Defense counsel — your motion to suppress the IP address logs. State your grounds.",
                "phase": "Motions",
            },
            {
                "agent": "Defense",
                "text": "Your Honor, St. Jude's IT department generated these logs internally. No third-party records custodian has authenticated them. Under FRE 803(6), the proponent must show the record was made at or near the time by someone with knowledge. The prosecution has not provided a witness from St. Jude's to lay that foundation.",
                "phase": "Motions",
            },
            {
                "agent": "Prosecutor",
                "text": "The People will call St. Jude's IT Director during trial to authenticate the logs. The records were generated automatically by the hospital's network monitoring system in the regular course of business. FRE 803(6) is satisfied with foundation witness testimony at trial.",
                "phase": "Motions",
            },
            {
                "agent": "Judge",
                "text": "Motion DENIED without prejudice. The defense may renew after foundation is laid at trial. The logs are conditionally admissible subject to authentication. FRE 104(b).",
                "phase": "Motions",
            },
            {
                "agent": "Prosecutor",
                "text": "The People move to preclude the defense from introducing evidence of the Berlin conference under FRE 403. The conference attendance does not prove Volkov was not at a keyboard — he could have used a VPN from Berlin. The probative value is substantially outweighed by the likelihood of jury confusion.",
                "phase": "Motions",
            },
            {
                "agent": "Defense",
                "text": "Objection, Your Honor. The conference evidence is central to our alibi defense. Physical presence in Berlin directly contradicts the claim that he operated the laptop from within the United States. VPN evidence is speculative — the prosecution has no VPN logs linking him.",
                "phase": "Motions",
            },
            {
                "agent": "Judge",
                "text": "Motion DENIED. The conference evidence is highly probative of the defense's theory. The prosecution may argue the VPN possibility to the jury — that goes to weight, not admissibility.",
                "phase": "Motions",
            },
            # ════════════════ PHASE 3: OPENING STATEMENTS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to opening statements.", "phase": "Opening"},
            {"agent": "Judge", "text": "Mr. Mercer — the People's opening statement.", "phase": "Opening"},
            {
                "agent": "Prosecutor",
                "text": "Ladies and gentlemen — on July 12th, at 2:14 AM, a ransomware attack encrypted 14,000 patient records at St. Jude's Medical Center. The hospital's systems were locked. Surgeries were cancelled. The attackers demanded $4.2 million in Bitcoin. The FBI traced the attack to a laptop owned by Dmitri Volkov, found his SSH keys loaded on the hospital's server, and followed the Bitcoin payments to an exchange account registered in his name. The evidence will show that Dmitri Volkov launched this attack — and that his Berlin trip was a carefully planned alibi, not a defense. The evidence points to one conclusion: Guilty.",
                "phase": "Opening",
            },
            {"agent": "Judge", "text": "Defense counsel.", "phase": "Opening"},
            {
                "agent": "Defense",
                "text": "Members of the jury — the prosecution asks you to convict Dmitri Volkov because his name is on a laptop and his keys exist in a server. They cannot place his hands on a keyboard. They cannot produce a single witness who saw him commit this crime. Here is what they cannot explain: Dmitri was in Berlin. His passport proves it. His hotel proves it. His conference badge proves it. And months before this attack, a known remote access trojan was harvesting credentials from laptops exactly like his. Someone stole his keys. Someone used his laptop. But that someone was not Dmitri Volkov. The evidence raises reasonable doubt at every turn. You must find him Not Guilty.",
                "phase": "Opening",
            },
            # ════════════════ PHASE 4: EVIDENCE PRESENTATION ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to evidence presentation.", "phase": "Evidence"},
            {
                "agent": "Prosecutor",
                "text": "The People submit Exhibit A: the Dell XPS 15 laptop seized from Dmitri Volkov's residence, containing SSH private keys in the home directory's .ssh folder.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "Objection — chain of custody, Your Honor. The laptop was seized three weeks after the attack. There is no evidence the laptop was in the same condition as at the time of the intrusion. The FBI could not have preserved the exact state of the SSH keys.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "The laptop was seized pursuant to a warrant, imaged on-site, and the hash chain is documented in Agent Chen's forensic report. The chain of custody is continuous and verifiable.",
                "phase": "Evidence",
            },
            {
                "agent": "Judge",
                "text": "Overruled. The chain of custody is adequately documented. Any gaps go to weight, not admissibility. Exhibit A admitted.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "The People submit Exhibit B: IP address logs from St. Jude's network monitoring system, showing the intrusion originated from a VPN endpoint at 2:14 AM on July 12th.",
                "phase": "Evidence",
            },
            {"agent": "Judge", "text": "Exhibit B admitted subject to authentication.", "phase": "Evidence"},
            {
                "agent": "Prosecutor",
                "text": "The People submit Exhibit C: blockchain transaction records linking the ransom Bitcoin wallet to a cryptocurrency exchange account registered to Dmitri Volkov at the email address d.volkov@pm.me.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "Objection — foundation. The prosecution has not established that the exchange account was actually controlled by Volkov at the time of the transaction. An email address alone does not prove control. Accounts can be compromised.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "The exchange provided KYC records — verified identification, utility bills, and a linked bank account — all matching the defendant. The account was created six months before the attack.",
                "phase": "Evidence",
            },
            {
                "agent": "Judge",
                "text": "Overruled. The KYC records provide sufficient foundation. The defense may cross-examine on the possibility of account compromise. Exhibit C admitted.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "The defense submits Exhibit D: passport entry and exit stamps showing Dmitri Volkov entered Germany on July 10th and departed July 14th, placing him in Berlin during the July 12th attack.",
                "phase": "Evidence",
            },
            {"agent": "Judge", "text": "Exhibit D admitted without objection.", "phase": "Evidence"},
            {
                "agent": "Defense",
                "text": "The defense submits Exhibit E: Hotel InterContinental Berlin key card logs showing Volkov's room access on the morning of July 12th at 8:47 AM local time — which is 2:47 AM Eastern, 33 minutes after the attack began.",
                "phase": "Evidence",
            },
            {"agent": "Judge", "text": "Exhibit E admitted without objection.", "phase": "Evidence"},
            # ════════════════ PHASE 5: WITNESS EXAMINATION ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to witness examination.", "phase": "Witness"},
            # --- FBI Digital Forensics Agent Chen ---
            {
                "agent": "Prosecutor",
                "text": "The People call Special Agent Marcus Chen, FBI Digital Forensics Unit. Agent Chen — describe your qualifications.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I hold a Master's degree in Cybersecurity from Carnegie Mellon. I have 12 years of experience in digital forensics, am a Certified Forensic Computer Examiner (CFCE), and have testified as an expert in 23 federal cases involving computer intrusion.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "Defense — voir dire?",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Agent Chen — your 23 prior testimonies, how many were for the prosecution and how many for the defense?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "All 23 were for the government. I am employed by the FBI. I do not provide expert services to criminal defendants.",
                "phase": "Witness",
            },
            {"agent": "Defense", "text": "No further on qualifications.", "phase": "Witness"},
            {
                "agent": "Judge",
                "text": "The court qualifies Special Agent Chen as an expert in digital forensics under FRE 702. You may proceed.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Agent Chen — describe what you found on Volkov's laptop.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The laptop contained SSH private keys in the standard .ssh/id_rsa path. I matched the public key to an entry in St. Jude's authorized_keys file on the compromised server. The key was added six weeks before the attack. I also found cryptocurrency wallet software and logs showing connection attempts to the same exchange address used in the ransom demand.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Could the keys have been added to the server by someone other than Volkov?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The SSH protocol authenticates by possession of the private key. If the key is on Volkov's laptop, it could only be used by someone with access to that laptop — or someone who copied the key file.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Testimony consistent with forensic report. Key matching confirmed.",
                "phase": "Witness",
            },
            # --- Cross: Agent Chen ---
            {
                "agent": "Defense",
                "text": "Agent Chen — you testified the key could be used by someone who copied the key file. Is there any forensic evidence — any log, any access record — showing that Volkov's specific laptop was used to authenticate to the server at 2:14 AM on July 12th?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The SSH protocol does not log which client device presented the key. We know the key was used from an IP address routed through a VPN. We cannot identify the specific device.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "So for all you know, the key could have been presented from a device in Berlin — or Singapore — or anywhere in the world with an internet connection?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Theoretically, yes. The key authenticates the user, not the device.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "And when you imaged this laptop three weeks after the attack — did you check whether it was infected with a remote access trojan?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I ran standard malware scans. No active RAT was detected at the time of imaging. I cannot rule out that one existed previously and was removed.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "No further questions.",
                "phase": "Witness",
            },
            # --- Redirect: Agent Chen ---
            {
                "agent": "Prosecutor",
                "text": "Agent Chen — one question on redirect. The laptop's SSH keys. You said they could have been copied. But the authorized_keys file on St. Jude's server was modified at 2:14 AM on July 12th — the exact time of the attack. If Volkov's keys were harvested by a RAT months before, why would the attacker wait until July 12th to add them to the server?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "That is a question of timing I cannot answer. The keys were added at the same time the attack began. It is consistent with a planned operation.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Timing observation is consistent with forensic timeline.",
                "phase": "Witness",
            },
            # --- Hospital IT Director ---
            {
                "agent": "Prosecutor",
                "text": "The People call David Okonkwo, IT Director at St. Jude's Medical Center. Mr. Okonkwo — describe the impact of the July 12th ransomware attack.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "At approximately 2:14 AM, our network monitoring system alerted on unusual encryption activity. By 2:18 AM, 14,000 patient records were encrypted. We had to cancel 23 scheduled surgeries, divert emergency patients to other hospitals, and shut down our entire network for 72 hours.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Did your system log the IP address that initiated the encryption?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes, our logs capture all inbound SSH connections. The encryption was initiated from an IP address traced to a VPN provider based in Panama. The VPN provider's logs — which we obtained through a mutual legal assistance request — show the connection originated from an IP range assigned to a Berlin-based ISP.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ MLAT response documented in evidence. Berlin ISP confirmed.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Mr. Okonkwo — the VPN provider's logs showed a Berlin ISP. Berlin is a city of 3.6 million people. That log does not identify my client. And a VPN can make traffic appear to originate from any city the provider chooses. Correct?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "That is correct. A VPN user can select their exit node. The Berlin ISP log places the connection in Berlin's general geographic area — it is not device-specific.",
                "phase": "Witness",
            },
            # --- Defense Expert: Dr. Amina Patel ---
            {
                "agent": "Defense",
                "text": "The defense calls Dr. Amina Patel, Associate Professor of Cybersecurity at Georgia Tech. Dr. Patel — please state your qualifications.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I hold a Ph.D. in Computer Science from MIT, specializing in network security and malware analysis. I have 15 years of research experience, have published 30 peer-reviewed papers on credential theft and remote access trojans, and have served as a court-appointed expert in three federal computer crime cases.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "Prosecution — voir dire?",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Patel — you were retained by the defense for this case, correct? And your fee is $650 per hour?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes, I was retained by defense counsel. My rate is standard for an expert of my seniority in cybersecurity litigation.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "No further on qualifications.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "The court qualifies Dr. Patel as an expert in cybersecurity under FRE 702.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Patel — the Dell XPS 15 laptop model. Is there a known vulnerability that allows credential harvesting?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. The XPS 15 with the 2022 BIOS version had a documented vulnerability — CVE-2022-33180 — that allows an attacker with physical access to boot from a USB device and copy the entire contents of the SSD, including SSH keys, without knowing the user password. The vulnerability was unpatched on the seized laptop.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Could Volkov's keys have been copied without his knowledge?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. If someone had physical access to the laptop for approximately 90 seconds, they could boot from a USB key, mount the SSD, copy the .ssh directory, and reboot. The laptop would show no signs of tampering.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ CVE-2022-33180 confirmed in NVD database. Unpatched status verified.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Patel — your theory requires someone to have physical access to Volkov's laptop. The FBI found no evidence of a break-in, no unauthorized access logs, and no witness placing anyone near Volkov's belongings. Is there any actual evidence that this vulnerability was exploited?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The nature of this exploit is that it leaves no trace. The absence of evidence of exploitation is consistent with the exploit's design. I cannot prove it happened — but the defense does not have to. The prosecution must prove beyond reasonable doubt that it did NOT happen, and the vulnerability makes that impossible.",
                "phase": "Witness",
            },
            # --- Alibi: Berlin Conference Coordinator ---
            {
                "agent": "Defense",
                "text": "The defense calls Ms. Hannah Berger, Event Coordinator for DevSecOps Berlin. Ms. Berger — was Dmitri Volkov present at the conference on July 12th?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. Our badge scanning system recorded his entry at 8:15 AM local time. He attended the morning keynote, the container security workshop from 10:00 AM to 12:00 PM, and the networking lunch. The badge logs show continuous scans at session entrances throughout the day.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Ms. Berger — the attack occurred at 2:14 AM Eastern Time, which is 8:14 AM in Berlin. Your badge scan shows entry at 8:15 AM — one minute after the attack began. Could he have used a laptop at 8:14 AM while walking into the conference venue?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "He could have been on his phone or a laptop simultaneously, yes. The badge scan does not preclude that.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Badge logs verified by conference organizer. Timestamps consistent.",
                "phase": "Witness",
            },
            # ════════════════ PHASE 6: REBUTTAL EVIDENCE ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to rebuttal evidence.", "phase": "Rebuttal"},
            {"agent": "Judge", "text": "Prosecution — rebuttal?", "phase": "Rebuttal"},
            {
                "agent": "Prosecutor",
                "text": "The defense has suggested a RAT and a credential harvesting exploit. But we note: the laptop was seized THREE WEEKS after the attack. The defense's own expert admitted she found no evidence of a RAT. And the KYC records for the Bitcoin exchange show the account was verified with Volkov's driver's license — not a stolen credential. The defense offers speculation, not evidence.",
                "phase": "Rebuttal",
            },
            {"agent": "Judge", "text": "Defense — surrebuttal?", "phase": "Rebuttal"},
            {
                "agent": "Defense",
                "text": "The prosecution shifts the burden. We do not need to prove the RAT existed — we only need to show it is possible. The CVE vulnerability proves credential theft is possible. The Berlin alibi proves my client was 4,000 miles away. The prosecution cannot exclude the reasonable hypothesis that someone else used his credentials from Berlin or elsewhere.",
                "phase": "Rebuttal",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Both sides presented arguments on burden of proof. Matter for jury.",
                "phase": "Rebuttal",
            },
            # ════════════════ PHASE 7: CLOSING ARGUMENTS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to closing arguments.", "phase": "Closing"},
            {
                "agent": "Prosecutor",
                "text": "Ladies and gentlemen — Dmitri Volkov's SSH keys were used to break into St. Jude's hospital. His laptop contained those keys. His Bitcoin account received the ransom. The timing of the attack — 2:14 AM, 8:14 AM Berlin time — placed him walking into a conference precisely when the attack launched. A convenient coincidence? Or a planned alibi? The VPN Berlin log says the attack came from Berlin. The hotel key card says he returned to his room at 8:47 AM. The defense's RAT theory is speculation — no evidence. The CVE exploit requires physical access, and there is no evidence anyone touched his laptop. The evidence is overwhelming. Find Dmitri Volkov Guilty.",
                "phase": "Closing",
            },
            {
                "agent": "Defense",
                "text": "The prosecution asks you to fill gaps with suspicion. A laptop with keys — yes. But whose hands used those keys? The prosecution cannot answer that. An exchange account in his name — yes. But exchange accounts are compromised every day, and the prosecution brought no evidence that he initiated the transaction. A Berlin VPN log — the same VPN that could route from anywhere. The standard is beyond reasonable doubt. Not 'probably.' Not 'likely.' Beyond reasonable doubt. The prosecution has not excluded the possibility that Dmitri's keys were stolen, his account was compromised, and someone else — from anywhere in the world — committed this crime. Reasonable doubt exists. You must find Dmitri Volkov Not Guilty.",
                "phase": "Closing",
            },
            # ════════════════ PHASE 8: JURY INSTRUCTIONS ════════════════
            {
                "agent": "Bailiff",
                "text": "The court will now proceed to jury instructions.",
                "phase": "Jury Instructions",
            },
            {
                "agent": "Judge",
                "text": "Members of the jury — Count One charges the defendant with Computer Intrusion under 18 U.S.C. § 1030(a)(2)(C). To find the defendant guilty, the prosecution must prove beyond a reasonable doubt: (1) the defendant intentionally accessed a protected computer without authorization; (2) the access obtained information from the computer; and (3) the conduct caused damage. Count Two charges Attempted Extortion under 18 U.S.C. § 1951. To find the defendant guilty, the prosecution must prove beyond a reasonable doubt that the defendant demanded property with intent to use fear of economic harm to induce compliance. Circumstantial evidence alone may be sufficient for conviction only if it excludes every reasonable hypothesis of innocence. The defendant is presumed innocent. If you have a reasonable doubt, you must acquit.",
                "phase": "Jury Instructions",
            },
            # ════════════════ PHASE 9: JURY DELIBERATION ════════════════
            {
                "agent": "Bailiff",
                "text": "The court will now proceed to jury deliberation.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Let us begin. Please state your initial positions.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #1 (Analytical): Not Guilty. The SSH key proves the key was used — not that Volkov used it. The prosecution did not exclude remote theft. The CVE vulnerability is a documented fact.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #2 (Skeptical): Guilty. The Bitcoin exchange KYC is strong evidence. It's not just the key — it's the money trail. The account was verified with his ID and bank account. That is hard to explain away.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #3 (Empathetic): Not Guilty. The Berlin alibi is convincing. Passport stamps, hotel key cards, conference badge scans. Being 4,000 miles away at the time of the crime is a powerful fact.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #4 (Pragmatic): Undecided. The digital evidence is strong but the alibi is also strong. I need to think about the timing more carefully.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Round 1: 2 Not Guilty, 1 Guilty, 1 Undecided. Let's discuss the exchange account. Juror #2 — can the money trail alone overcome the alibi?",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #2: The KYC process requires photo ID. The attacker would need Volkov's physical driver's license to open that account. That's hard to fake. But... the account was opened six months before the attack. It could have been taken over by someone else later.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #4: I keep coming back to the standard. Beyond reasonable doubt. The defense showed a real vulnerability. A real alibi. A real alternative explanation. I'm Not Guilty.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Round 2: 3 Not Guilty, 1 Guilty. Juror #2 — further thoughts?",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #2: The hospital suffered real damage. But the judge said circumstantial must exclude every reasonable hypothesis. The CVE exploit is a reasonable hypothesis. I change my vote to Not Guilty.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Round 3: 4 Not Guilty, 0 Guilty. Unanimous verdict reached.",
                "phase": "Jury Deliberation",
            },
            # ════════════════ PHASE 10: SHADOW JURY ════════════════
            {"agent": "Bailiff", "text": "The shadow jury has convened for analysis.", "phase": "Shadow Jury"},
            {
                "agent": "Juror",
                "text": "Shadow Juror 1: The Berlin alibi is strong physical evidence. Passport stamps and hotel records are not easily faked. The prosecution's VPN theory is speculative. [Vote: Not Guilty]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 2: Digital credentials can be stolen without the owner's knowledge. The CVE vulnerability is documented and the laptop was not patched. The prosecution did not exclude this. [Vote: Not Guilty]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 3: The Bitcoin trail is concerning. KYC verification with real ID is significant. But the alibi and the credential theft possibility create reasonable doubt. [Vote: Not Guilty]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 4: Without a witness placing Volkov at the keyboard, this is entirely circumstantial. The standard is beyond reasonable doubt — not met here. [Vote: Not Guilty]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 5: The timing is suspicious — attack at 2:14 AM, hotel key at 2:47 AM local. But suspicion is not proof. The defense raised sufficient doubt. [Vote: Not Guilty]",
                "phase": "Shadow Jury",
            },
            {"agent": "Bailiff", "text": "The shadow jury has completed its analysis.", "phase": "Shadow Jury"},
            # ════════════════ PHASE 11: VERDICT ════════════════
            {"agent": "Bailiff", "text": "All rise for the reading of the verdict.", "phase": "Verdict"},
            {
                "agent": "Judge",
                "text": "On Count One — Computer Intrusion — the defendant Dmitri Volkov is found NOT GUILTY. On Count Two — Attempted Extortion — the defendant Dmitri Volkov is found NOT GUILTY. The defendant is free to go.",
                "phase": "Verdict",
            },
            # ════════════════ PHASE 12: COURT REPORTER ════════════════
            {
                "agent": "Bailiff",
                "text": "Case 24-CR-0194 — State of New York versus Dmitri Volkov — is concluded. The trial record shall be certified by the court reporter.",
                "phase": "Court Reporter Log",
            },
            {
                "agent": "System",
                "text": "[Court Reporter Log: Complete trial record compiled. Case 24-CR-0194. Verdict: NOT GUILTY on all counts. Transcript includes 5 exhibits, 4 witnesses including 1 expert qualification, 2 pre-trial motions, 6 objections with rulings, 6-phase trial, 5 shadow juror analyses.]",
                "phase": "Court Reporter Log",
            },
            # ════════════════ ADJOURNED ════════════════
            {
                "agent": "Bailiff",
                "text": "All charges have been adjudicated. This court is adjourned.",
                "phase": "Adjourned",
            },
        ],
        "verdict": "NOT GUILTY",
        "win_probability": 0.31,
        "sensitivity": "If Volkov's laptop had full-disk encryption enabled → Prosecution win probability rises to 74%",
        "shadow_jury_narrative": [
            {
                "name": "Shadow Juror 1",
                "content": "The Berlin alibi is strong physical evidence. Passport stamps and hotel records are not easily faked. The prosecution's VPN theory is speculative. [Vote: Not Guilty]",
            },
            {
                "name": "Shadow Juror 2",
                "content": "Digital credentials can be stolen without the owner's knowledge. The CVE vulnerability is documented and the laptop was not patched. The prosecution did not exclude this. [Vote: Not Guilty]",
            },
            {
                "name": "Shadow Juror 3",
                "content": "The Bitcoin trail is concerning. KYC verification with real ID is significant. But the alibi and the credential theft possibility create reasonable doubt. [Vote: Not Guilty]",
            },
            {
                "name": "Shadow Juror 4",
                "content": "Without a witness placing Volkov at the keyboard, this is entirely circumstantial. The standard is beyond reasonable doubt — not met here. [Vote: Not Guilty]",
            },
            {
                "name": "Shadow Juror 5",
                "content": "The timing is suspicious — attack at 2:14 AM, hotel key at 2:47 AM local. But suspicion is not proof. The defense raised sufficient doubt. [Vote: Not Guilty]",
            },
        ],
    },
    "spill": {
        "title": "Coastal Protection Agency v. Meridian Oil — Toxic Spill Cover-Up",
        "jurisdiction": "United States · Federal District Court, Eastern District",
        "description": (
            "The Coastal Protection Agency alleges Meridian Oil is liable for an 80,000-gallon "
            "crude oil spill that devastated the Point Reyes Marine Sanctuary on March 3rd. "
            "A whistleblower — former Meridian engineer James Okafor — provided internal emails "
            "showing that Meridian's inspection team discovered severe pipe corrosion six weeks "
            "before the spill but senior management deferred the $2 million repair to meet "
            "quarterly earnings targets. Satellite imagery from NOAA confirms the spill trajectory "
            "originating from Meridian's offshore Platform Charlie. Meridian claims the pipe failure "
            "was unforeseeable, that its maintenance schedule met all federal regulatory standards, "
            "and that the whistleblower is a disgruntled former employee seeking retaliation."
        ),
        "questions": [
            "When was the pipe corrosion first documented in Meridian's internal inspection reports?",
            "Did Meridian receive a specific written recommendation to shut down Pipeline 7-A?",
            "Can satellite imagery definitively attribute the spill to Meridian's Platform Charlie?",
            "What was the quantified economic damage to local fishing and tourism industries?",
            "Did Meridian's maintenance schedule comply with federal Pipeline Safety Act standards?",
        ],
        "trial_script": [
            # ════════════════ PHASE 1: DISCOVERY ════════════════
            {
                "agent": "Bailiff",
                "text": "All rise. The Honorable Justice Cross presiding. The court is now in session for the Discovery Disclosure phase.",
                "phase": "Discovery",
            },
            {
                "agent": "Judge",
                "text": "Be seated. Coastal Protection Agency versus Meridian Oil Corporation — civil action for environmental damages under the Clean Water Act. Plaintiff's counsel, your disclosure.",
                "phase": "Discovery",
            },
            {
                "agent": "Prosecutor",
                "text": "The plaintiff discloses: (1) Internal Meridian emails from February 3rd documenting severe corrosion on Pipeline 7-A, with recommendation to shut down; (2) NOAA satellite imagery time series from March 3rd showing the spill trajectory from Platform Charlie; (3) Expert report by Dr. Elena Vasquez, marine toxicologist, quantifying ecological damage; (4) Whistleblower deposition of James Okafor, former Meridian senior pipeline engineer.",
                "phase": "Discovery",
            },
            {
                "agent": "Defense",
                "text": "Meridian Oil discloses: (1) Inspection reports confirming all regulatory maintenance schedules were met; (2) Expert report by Dr. Robert Kim, mechanical engineer, concluding the pipe corrosion was not detectable by standard inspection methods; (3) James Okafor's termination letter for violation of non-disclosure agreement; (4) Third-party audit showing Pipeline 7-A met all Pipeline Safety Act requirements.",
                "phase": "Discovery",
            },
            {
                "agent": "Judge",
                "text": "Disclosure is complete. The court notes the central dispute: whether the pipe failure was foreseeable. Proceed to pre-trial motions.",
                "phase": "Discovery",
            },
            # ════════════════ PHASE 2: PRE-TRIAL MOTIONS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to pre-trial motions.", "phase": "Motions"},
            {
                "agent": "Judge",
                "text": "Defense counsel — your motion to exclude the whistleblower emails. State your grounds.",
                "phase": "Motions",
            },
            {
                "agent": "Defense",
                "text": "Your Honor, James Okafor was terminated for violating his NDA. The emails he provided were obtained in violation of his contractual obligations. Under Federal common law, evidence obtained in breach of a confidentiality agreement should be excluded to avoid incentivizing contractual breaches.",
                "phase": "Motions",
            },
            {
                "agent": "Prosecutor",
                "text": "The emails are not privileged. Okafor had a reasonable belief of ongoing illegality — the emails show decisions that would lead to environmental harm. This falls within the whistleblower exception to confidentiality obligations. Additionally, the emails are Meridian's own business records — they are admissible as party-opponent statements under FRE 801(d)(2).",
                "phase": "Motions",
            },
            {
                "agent": "Judge",
                "text": "Motion DENIED. The emails are Meridian's own communications — they are party-opponent statements under FRE 801(d)(2)(A). Okafor's NDA is a separate contractual matter between him and Meridian, not a ground for evidentiary exclusion. The emails are admissible.",
                "phase": "Motions",
            },
            {
                "agent": "Prosecutor",
                "text": "The plaintiff moves for partial summary judgment on the issue of liability. The internal emails show Meridian had actual knowledge of the corrosion and chose not to act. No reasonable jury could find the spill unforeseeable.",
                "phase": "Motions",
            },
            {
                "agent": "Defense",
                "text": "Meridian opposes. There is a genuine dispute of material fact: whether the corrosion was severe enough to require immediate shutdown. Meridian's engineering team believed the pipe could safely operate until the scheduled maintenance window. That is a jury question.",
                "phase": "Motions",
            },
            {
                "agent": "Judge",
                "text": "Summary judgment DENIED. The severity of the corrosion and the reasonableness of Meridian's decision are disputed facts for the jury. Proceed to trial.",
                "phase": "Motions",
            },
            # ════════════════ PHASE 3: OPENING STATEMENTS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to opening statements.", "phase": "Opening"},
            {"agent": "Judge", "text": "Plaintiff's counsel — opening statement, please.", "phase": "Opening"},
            {
                "agent": "Prosecutor",
                "text": "Ladies and gentlemen — on March 3rd, eighty thousand gallons of crude oil spilled into the Point Reyes Marine Sanctuary — one of America's most protected waters. The oil killed seabirds, contaminated oyster beds, and closed 200 square miles of ocean to fishing. But here is what makes this case different: Meridian Oil knew this would happen. Six weeks before the spill, their own inspection team found severe corrosion on Pipeline 7-A. Their own engineers recommended shutting it down. And their own executives said no — because fixing it would cost $2 million and hurt their quarterly earnings. The internal emails prove it. The satellite imagery proves the spill came from their platform. The damage is documented. By a preponderance of the evidence, Meridian Oil is liable.",
                "phase": "Opening",
            },
            {
                "agent": "Judge",
                "text": "Defense counsel.",
                "phase": "Opening",
            },
            {
                "agent": "Defense",
                "text": "Members of the jury — the plaintiff wants you to believe that one email is proof of negligence. But Meridian Oil operates 47 offshore platforms, 2,000 miles of pipeline, and conducts over 15,000 inspections a year. Every pipeline has some degree of corrosion — it is a natural consequence of transporting hydrocarbons. The question is not whether corrosion existed. The question is whether the corrosion was severe enough to present an imminent risk. Meridian's engineers — experts with decades of experience — determined it was not. The pipe was scheduled for replacement in the normal maintenance cycle. What happened was a tragic but unforeseeable failure. Liability requires foreseeability. Meridian is not liable.",
                "phase": "Opening",
            },
            # ════════════════ PHASE 4: EVIDENCE PRESENTATION ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to evidence presentation.", "phase": "Evidence"},
            {
                "agent": "Prosecutor",
                "text": "Plaintiff submits Exhibit A: internal Meridian emails dated February 3rd, from lead inspector Dan Torres to VP of Operations Karen Sims, stating 'Pipeline 7-A corrosion is at 78% wall loss — recommend immediate shutdown and replacement.'",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "Objection, Your Honor. Authentication — the plaintiff has not established that these emails are authentic business records. No Meridian custodian has verified them.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "James Okafor will authenticate the emails during his testimony. He was copied on the email chain and was present at the meeting where the recommendation was discussed.",
                "phase": "Evidence",
            },
            {
                "agent": "Judge",
                "text": "Conditionally admitted subject to Okafor's authentication. FRE 104(b). Exhibit A admitted subject to connection.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "Plaintiff submits Exhibit B: NOAA satellite imagery from March 3rd, 8:00 PM UTC, showing the oil slick originating from Platform Charlie and spreading northeast toward the sanctuary at 2.5 knots.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "Objection — foundation. The NOAA analyst who processed these images is not here to testify. The images are hearsay within a public record.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "Satellite imagery is not hearsay — it is a photograph, a thing not a statement. And NOAA's public records are self-authenticating under FRE 902(11). There is no hearsay issue.",
                "phase": "Evidence",
            },
            {
                "agent": "Judge",
                "text": "Overruled. Satellite imagery is demonstrative evidence, not hearsay. The NOAA certification is sufficient for self-authentication under FRE 902. Exhibit B admitted.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "The defense submits Exhibit C: Meridian's third-party pipeline safety audit, dated January 15th, concluding Pipeline 7-A met all federal Pipeline Safety Act requirements and had an estimated remaining safe life of 14 months.",
                "phase": "Evidence",
            },
            {"agent": "Judge", "text": "Exhibit C admitted without objection.", "phase": "Evidence"},
            # ════════════════ PHASE 5: WITNESS EXAMINATION ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to witness examination.", "phase": "Witness"},
            # --- Whistleblower: James Okafor ---
            {
                "agent": "Prosecutor",
                "text": "The plaintiff calls James Okafor. Mr. Okafor — you were a senior pipeline engineer at Meridian Oil until February 28th. Describe your role.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I was responsible for inspecting Meridian's offshore pipeline infrastructure. I supervised a team of four inspectors covering 22 pipelines across the Gulf region.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Tell the jury about the February 3rd meeting regarding Pipeline 7-A.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I presented the inspection findings to VP Karen Sims. The ultrasonic testing showed 78% wall loss on a 20-inch diameter pipe. Industry standard recommends shutdown at 70% wall loss. I recommended immediate shutdown. Ms. Sims said the cost of shutting down Platform Charlie for two weeks — approximately $2 million in lost production — was unacceptable. She wanted to defer until the Q3 maintenance cycle.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Did you express concern about this decision in writing?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. I sent an email to Ms. Sims later that day — Exhibit A — reiterating that operating at 78% wall loss was unsafe and that I could not recommend continued operation. I copied my personal email as a record.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Email chain verified. 78% wall loss confirmed in inspection report.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Mr. Okafor — you were fired from Meridian Oil on February 28th, correct?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. They terminated me for violating the NDA by forwarding company emails to my personal account.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "And you are currently suing Meridian for wrongful termination, seeking $2.3 million in damages?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. I have a pending lawsuit. But that does not change the facts of what I found and what I reported.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "You stand to gain financially from a verdict against Meridian, correct?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "My wrongful termination case is separate from this litigation. I am not a party to this lawsuit.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Witness has disclosed financial interest in related litigation. Credibility matter for jury.",
                "phase": "Witness",
            },
            # --- Expert: Dr. Elena Vasquez (marine toxicologist) ---
            {
                "agent": "Prosecutor",
                "text": "The plaintiff calls Dr. Elena Vasquez, Professor of Marine Toxicology at UC Santa Barbara. Dr. Vasquez — your qualifications?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I hold a Ph.D. in Marine Biology from Stanford. I have 18 years of research experience in marine oil spill impact assessment, have authored 45 peer-reviewed publications, and have served as a scientific advisor on four major oil spill response efforts including Deepwater Horizon and Refugio.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "Defense — voir dire?",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Vasquez — your research is primarily funded through federal grants. You have never worked for an oil company. Is it fair to say your career has focused on demonstrating the negative environmental impacts of oil extraction?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "My career has focused on understanding the environmental impacts of marine pollution, including oil spills. I apply the scientific method regardless of who funds the research.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "No further on qualifications.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "The court qualifies Dr. Vasquez as an expert in marine toxicology under FRE 702. You may proceed.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Vasquez — describe the ecological impact of the March 3rd spill.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The 80,000-gallon crude oil release affected approximately 200 square miles of marine habitat. My analysis documents: 2,400 seabird deaths, contamination of 18 commercial oyster beds, a 60% reduction in plankton productivity in the affected zone, and long-term toxicity in sediment samples that will persist for 7 to 12 years. The economic damage to local fisheries is estimated at $4.7 million in lost revenue over the first year alone.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Could this damage have been prevented?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "If the pipeline had been shut down when the corrosion was discovered, the spill would not have occurred. The damage is entirely attributable to the failure to act on known information.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Economic data sourced from NOAA fisheries survey. Sediment analysis methodology peer-reviewed.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Vasquez — your $4.7 million figure assumes the fishery would have operated at full capacity for the entire year. But the spill occurred during spawning season when many fisheries are voluntarily restricted. Your baseline is overstated, correct?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I applied NOAA's standard fisheries economic impact model. The $4.7 million accounts for seasonal variation. The loss is real and documented.",
                "phase": "Witness",
            },
            # --- Defense Expert: Dr. Robert Kim ---
            {
                "agent": "Defense",
                "text": "The defense calls Dr. Robert Kim, Professor of Mechanical Engineering at Texas A&M. Dr. Kim — your qualifications?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I hold a Ph.D. in Mechanical Engineering from MIT. I have 25 years of experience in pipeline integrity and corrosion engineering. I have consulted for the Pipeline Safety Trust, the American Petroleum Institute, and have served as an expert in 12 pipeline failure cases.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "Prosecution — voir dire?",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Kim — you have consulted for the American Petroleum Institute, which is the primary lobbying organization for the oil and gas industry. Is that correct?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "API develops industry standards for pipeline safety. My work for API involved helping develop those standards — not lobbying.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "No further on qualifications.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "The court qualifies Dr. Kim as an expert in pipeline engineering under FRE 702.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Kim — in your opinion, was Meridian's decision to defer the Pipeline 7-A repair reasonable?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. Industry standard for wall loss shutdown is 80% — Meridian's own audit found 78%, which is within the acceptable operating range. The third-party safety audit confirmed a remaining safe life of 14 months. The decision to defer to Q3, a six-month delay, was well within the margin of safety.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Kim — Okafor testified that Meridian's internal standard was 70% wall loss for shutdown. Are you saying the internal standard was wrong?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I am saying the internal standard was more conservative than industry practice. Operating at 78% with 14 months of remaining safe life was not a safety violation. Hindsight is 20/20 — after a catastrophic failure, any corrosion level looks dangerous. The question is whether Meridian's decision was reasonable based on what they knew at the time.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "But you admit the pipe DID fail. The three-month deferral was not six months — it was three weeks before the scheduled shutdown. The corrosion was clearly worse than your 'remaining safe life' estimate. Your model was wrong, was it not?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The failure was a rare event. Corrosion models predict statistical probability — they do not guarantee outcomes. A pipe rated for 14 months of safe life can fail at any time due to localized anomalies that standard ultrasonic testing cannot detect. That does not mean the decision to defer was unreasonable.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Both experts disagree on industry standard threshold. Jury may weigh competing testimony.",
                "phase": "Witness",
            },
            # ════════════════ PHASE 6: REBUTTAL EVIDENCE ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to rebuttal evidence.", "phase": "Rebuttal"},
            {"agent": "Judge", "text": "Plaintiff — rebuttal?", "phase": "Rebuttal"},
            {
                "agent": "Prosecutor",
                "text": "Dr. Kim says 78% was acceptable. But Meridian's OWN engineers recommended shutdown at 70%. The defense asks you to believe an industry standard that starts at 80% — conveniently above Meridian's actual reading. And Dr. Kim's '14-month safe life' — where did that come from? The third-party audit was paid for by Meridian, conducted by a firm Meridian hires annually. Their estimate was wrong. The pipe failed in 3 weeks. The defense's expert was wrong.",
                "phase": "Rebuttal",
            },
            {"agent": "Judge", "text": "Defense — surrebuttal?", "phase": "Rebuttal"},
            {
                "agent": "Defense",
                "text": "The plaintiff asks you to infer negligence from a pipe failure. But negligence requires foreseeability, not hindsight. Every pipeline engineer in the country will tell you that pipes fail — even well-maintained ones. Corrosion is measured in probabilities, not certainties. Meridian followed industry standards, passed third-party audits, and made a reasonable engineering judgment. The fact that a rare failure occurred is not evidence of negligence.",
                "phase": "Rebuttal",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Both expert opinions noted. Core dispute: reasonableness of maintenance decision.",
                "phase": "Rebuttal",
            },
            # ════════════════ PHASE 7: CLOSING ARGUMENTS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to closing arguments.", "phase": "Closing"},
            {
                "agent": "Prosecutor",
                "text": "Ladies and gentlemen — this case is about a choice. Meridian Oil knew about the corrosion. Their own engineers told them to shut it down. And they chose profit over safety. $2 million to fix the pipe. $4.7 million in damages after the spill. An email trail that documents every decision. The defense will tell you about industry standards — but their own standard was higher. The defense will tell you about reasonable engineering judgment — but their engineers recommended shutdown. The standard is preponderance of the evidence — more likely than not. Is it more likely than not that Meridian's decision to defer caused this spill? The emails say yes. The science says yes. The damage says yes. Find Meridian Oil Liable.",
                "phase": "Closing",
            },
            {
                "agent": "Defense",
                "text": "The plaintiff wants you to punish Meridian because a pipe failed. But Meridian did everything right. They inspected regularly. They followed industry standards. They hired independent auditors. A pipe failed — tragically — but that is not the same as negligence. The plaintiff's case rests on one employee — James Okafor — who was fired for stealing company emails and is now suing Meridian for millions. His reliability is the foundation of their case. Dr. Kim explained that 78% wall loss is within industry norms. The third-party audit confirmed safety. Hindsight is not a legal basis for liability. By a preponderance of the evidence, Meridian acted reasonably. Find Meridian Oil Not Liable.",
                "phase": "Closing",
            },
            # ════════════════ PHASE 8: JURY INSTRUCTIONS ════════════════
            {
                "agent": "Bailiff",
                "text": "The court will now proceed to jury instructions.",
                "phase": "Jury Instructions",
            },
            {
                "agent": "Judge",
                "text": "Members of the jury — this is a civil action under the Clean Water Act. The plaintiff, Coastal Protection Agency, must prove its case by a preponderance of the evidence — meaning it is more likely than not that Meridian Oil is liable. To find Meridian liable, you must find: (1) Meridian owned or operated the pipeline that released oil; (2) the release caused damage to natural resources; and (3) Meridian failed to exercise reasonable care in maintaining the pipeline. Negligence is the failure to use ordinary care — that is, the care that a reasonably prudent pipeline operator would use under similar circumstances. The plaintiff does not need to prove that Meridian intended the harm — only that their failure to act reasonably caused the spill. Your verdict must be unanimous.",
                "phase": "Jury Instructions",
            },
            # ════════════════ PHASE 9: JURY DELIBERATION ════════════════
            {
                "agent": "Bailiff",
                "text": "The court will now proceed to jury deliberation.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Initial positions, please.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #1 (Analytical): Liable. The emails are damning. The company's own engineers said shut it down. Management chose money over safety. That is negligence.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #2 (Skeptical): Not Liable. Okafor has a financial motive. He is suing them. The independent audit said the pipe was safe. Dr. Kim was convincing that 78% is within norms.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #3 (Empathetic): Liable. Whether or not Okafor is biased, the emails exist. They show management knew and chose to defer. If they had acted, the spill does not happen.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #4 (Pragmatic): Liable. The economic damage is real. The question is whether Meridian's decision was reasonable. Choosing to defer a known risk for quarterly earnings — that is not reasonable care.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Round 1: 3 Liable, 1 Not Liable. Juror #2 — what would change your mind?",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #2: If the emails weren't there, I would be solidly Not Liable. But the emails are there. Management knew and chose cost over safety. It bothers me that Okafor is suing them, but the emails speak for themselves. I'll change to Liable.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Round 2: 4 Liable, 0 Not Liable. Unanimous verdict reached.",
                "phase": "Jury Deliberation",
            },
            # ════════════════ PHASE 10: SHADOW JURY ════════════════
            {"agent": "Bailiff", "text": "The shadow jury has convened for analysis.", "phase": "Shadow Jury"},
            {
                "agent": "Juror",
                "text": "Shadow Juror 1: The internal emails are the strongest evidence. Meridian's own engineers warned them. Management chose profit. Clear negligence. [Vote: Liable, confidence 92%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 2: Okafor's financial interest in the outcome is concerning. But the documentary evidence — emails, satellite imagery — stands independently of his testimony. [Vote: Liable, confidence 78%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 3: Expert disagreement centers on what standards apply. But even by industry standards, 78% wall loss with a recommendation to shut down creates liability when you choose to ignore it. [Vote: Liable, confidence 84%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 4: The $4.7 million economic damage is well-documented. The spill was preventable. The emails prove knowledge. This is a textbook case of corporate negligence. [Vote: Liable, confidence 91%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 5: Reasonable care requires listening to your engineers. Meridian did not. That failure caused 80,000 gallons of oil to destroy a marine sanctuary. The liability is clear. [Vote: Liable, confidence 87%]",
                "phase": "Shadow Jury",
            },
            {"agent": "Bailiff", "text": "The shadow jury has completed its analysis.", "phase": "Shadow Jury"},
            # ════════════════ PHASE 11: VERDICT ════════════════
            {"agent": "Bailiff", "text": "All rise for the reading of the verdict.", "phase": "Verdict"},
            {
                "agent": "Judge",
                "text": "The jury finds Meridian Oil Corporation LIABLE for violation of the Clean Water Act. We will now proceed to the damages phase.",
                "phase": "Verdict",
            },
            # ════════════════ PHASE 12: SENTENCING / DAMAGES ════════════════
            {
                "agent": "Bailiff",
                "text": "The court will now proceed to the damages assessment.",
                "phase": "Sentencing",
            },
            {
                "agent": "Judge",
                "text": "Having found Meridian liable, the court will assess civil penalties and damages. Plaintiff's counsel — your submission.",
                "phase": "Sentencing",
            },
            {
                "agent": "Prosecutor",
                "text": "Your Honor, the Clean Water Act authorizes civil penalties of up to $56,800 per barrel of oil discharged. Meridian discharged approximately 1,905 barrels. The statutory maximum is $108 million. However, the plaintiff requests $4.7 million in economic damages to the fishing and tourism industries, $12 million in ecological restoration costs, and a civil penalty of $8 million reflecting the gravity of Meridian's knowing conduct — total $24.7 million.",
                "phase": "Sentencing",
            },
            {
                "agent": "Judge",
                "text": "Defense counsel — your response on mitigation.",
                "phase": "Sentencing",
            },
            {
                "agent": "Defense",
                "text": "Your Honor, Meridian Oil has already spent $6.2 million on cleanup and containment. The company cooperated fully with the Coast Guard and NOAA. This was not a knowing discharge — it was an unforeseeable pipe failure. Meridian's 2,000-mile pipeline network has had zero spills in the past five years. The requested $24.7 million would force significant layoffs and facility closures in the Gulf region. We submit that $3 million in ecological restoration — which Meridian has already offered to fund voluntarily — plus a $2 million civil penalty is more than adequate.",
                "phase": "Sentencing",
            },
            {
                "agent": "Judge",
                "text": "The court has considered both submissions. Meridian Oil — your maintenance decision prioritized short-term cost savings over known safety risks. That knowing conduct distinguishes this case from a truly unforeseeable accident. However, the court also credits your cooperation with response efforts and your clean safety record prior to this incident. The court awards the following: $4.7 million in economic damages to affected fisheries and tourism businesses; $12 million in ecological restoration costs; and a civil penalty of $8 million. Total judgment: $24.7 million. Meridian Oil is further ordered to implement a revised pipeline inspection protocol at all offshore facilities within 180 days. This court is adjourned.",
                "phase": "Sentencing",
            },
            # ════════════════ PHASE 13: COURT REPORTER ════════════════
            {
                "agent": "Bailiff",
                "text": "Case 24-CV-0287 — Coastal Protection Agency versus Meridian Oil Corporation — is concluded. The trial record shall be certified by the court reporter.",
                "phase": "Court Reporter Log",
            },
            {
                "agent": "System",
                "text": "[Court Reporter Log: Complete trial record compiled. Case 24-CV-0287. Verdict: LIABLE. Damages: $24.7 million. Transcript includes 3 exhibits, 4 witnesses including 2 expert qualifications, 3 objections with rulings, 2 pre-trial motions, 4-phase adversarial process, 5 shadow juror analyses, full damages hearing.]",
                "phase": "Court Reporter Log",
            },
            # ════════════════ ADJOURNED ════════════════
            {
                "agent": "Bailiff",
                "text": "All matters have been adjudicated. This court is adjourned.",
                "phase": "Adjourned",
            },
        ],
        "verdict": "LIABLE",
        "win_probability": 0.78,
        "sensitivity": "If the whistleblower emails were ruled inadmissible → Plaintiff win probability drops to 44%",
        "sentence": {
            "sentence": "The court finds Meridian Oil liable under the Clean Water Act and awards damages.",
            "term": "$4.7 million economic damages, $12 million ecological restoration, $8 million civil penalty. Total: $24.7 million.",
            "rationale": "Meridian knowingly deferred pipeline repair despite engineer recommendation. Emails demonstrate conscious cost-benefit decision favoring profit over safety. Damage to Point Reyes Marine Sanctuary is extensive and documented.",
        },
        "shadow_jury_narrative": [
            {
                "name": "Shadow Juror 1",
                "content": "The internal emails are the strongest evidence. Meridian's own engineers warned them. Management chose profit. Clear negligence. [Vote: Liable]",
            },
            {
                "name": "Shadow Juror 2",
                "content": "Okafor's financial interest is concerning. But the documentary evidence stands independently. [Vote: Liable]",
            },
            {
                "name": "Shadow Juror 3",
                "content": "Even by industry standards, 78% wall loss with a recommendation to shut down creates liability when you choose to ignore it. [Vote: Liable]",
            },
            {
                "name": "Shadow Juror 4",
                "content": "The $4.7 million economic damage is well-documented. The spill was preventable. The emails prove knowledge. [Vote: Liable]",
            },
            {
                "name": "Shadow Juror 5",
                "content": "Reasonable care requires listening to your engineers. Meridian did not. That failure caused 80,000 gallons of oil to destroy a marine sanctuary. [Vote: Liable]",
            },
        ],
    },
    "clinical": {
        "title": "State v. Dr. Sarah Blake — Involuntary Manslaughter by Clinical Trial Misconduct",
        "jurisdiction": "United States · Federal District Court, Southern District of New York",
        "description": (
            "The defendant, Dr. Sarah Blake, is charged with one count of involuntary manslaughter "
            "(18 U.S.C. § 1112) and one count of reckless endangerment following the death of "
            "Marcus Chen, a 34-year-old participant in an unauthorized Phase I clinical trial. "
            "Blake, an oncologist at Northwell Health, administered an experimental immunotherapy "
            "drug — ONC-279 — to Chen without obtaining proper ethics committee approval. Chen died "
            "from cytokine storm syndrome 72 hours after infusion. Internal hospital records show "
            "Blake's ethics application was submitted to the IRB two days AFTER Chen received "
            "the first dose. The consent forms were backdated to appear signed before treatment "
            "began. The trial's dosing protocol deviated from the approved regimen: Blake "
            "administered 2.5x the maximum safe starting dose. Dr. Blake claims Chen was informed "
            "of the experimental nature and signed consent, and that the dosing was within her "
            "medical judgment as the principal investigator."
        ),
        "questions": [
            "When was the IRB application actually submitted relative to the first dose administered?",
            "Were the consent forms signed before or after the first dose based on document analysis?",
            "Did the administered dosing protocol match what was submitted in the IRB application?",
            "Had Dr. Blake conducted similar unauthorized trials at any other institution?",
            "Was the patient informed that the drug had never been tested in humans before?",
        ],
        "trial_script": [
            # ════════════════ PHASE 1: DISCOVERY ════════════════
            {
                "agent": "Bailiff",
                "text": "All rise. The Honorable Justice Vance presiding. The court is now in session for the Discovery Disclosure phase.",
                "phase": "Discovery",
            },
            {
                "agent": "Judge",
                "text": "Be seated. The matter of State versus Dr. Sarah Blake — involuntary manslaughter and reckless endangerment. The People will disclose first.",
                "phase": "Discovery",
            },
            {
                "agent": "Prosecutor",
                "text": "The People disclose: (1) IRB application records showing submission date of March 15th — two days after the first dose on March 13th; (2) Signed consent forms for Marcus Chen bearing the date March 12th, with ink analysis suggesting the dates were altered; (3) Pharmacy dispensing records showing ONC-279 was administered at 2.5x the maximum safe starting dose; (4) Medical examiner report confirming cytokine storm syndrome as cause of death; (5) Email correspondence from Dr. Blake to a colleague stating 'We can submit the IRB retroactively — the patient is too sick to wait.'",
                "phase": "Discovery",
            },
            {
                "agent": "Defense",
                "text": "The defense discloses: (1) Dr. Blake's expert report by Dr. Jonathan Weiss, clinical pharmacologist, concluding that 2.5x dose was within standard Phase I safety margins for patients with treatment-resistant cancer; (2) Marcus Chen's medical records documenting his stage IV metastatic disease and his documented verbal consent to 'try anything'; (3) Character references from 12 colleagues attesting to Dr. Blake's ethical conduct over 15 years of practice.",
                "phase": "Discovery",
            },
            {
                "agent": "Judge",
                "text": "Disclosure is complete. The court notes the central issue: whether Dr. Blake's deviation from protocol constitutes criminal negligence or a reasonable exercise of medical judgment. Proceed to pre-trial motions.",
                "phase": "Discovery",
            },
            # ════════════════ PHASE 2: PRE-TRIAL MOTIONS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to pre-trial motions.", "phase": "Motions"},
            {
                "agent": "Judge",
                "text": "Defense counsel — your motion to exclude the email as taken out of context. State your grounds.",
                "phase": "Motions",
            },
            {
                "agent": "Defense",
                "text": "Your Honor, the email states 'We can submit the IRB retroactively.' The prosecution presents this as evidence of intent to deceive. But in context, Dr. Blake was referring to the standard IRB modification process — where retrospective approval is permitted for urgent medical interventions under 21 CFR 56.104. The email is ambiguous and unfairly prejudicial under FRE 403.",
                "phase": "Motions",
            },
            {
                "agent": "Prosecutor",
                "text": "The email is a party-opponent statement under FRE 801(d)(2). Dr. Blake wrote it. She said 'retroactively.' That is her own words. The context will be explored at trial. But the statement itself is admissible as an admission.",
                "phase": "Motions",
            },
            {
                "agent": "Judge",
                "text": "Motion DENIED. The email is admissible as a party-opponent statement. The defense may present contextual evidence at trial. The jury will weigh the meaning.",
                "phase": "Motions",
            },
            {
                "agent": "Prosecutor",
                "text": "The People move to admit Dr. Blake's prior disciplinary history from New York Presbyterian Hospital regarding an unauthorized research study in 2018, under FRE 404(b) to show pattern of conduct.",
                "phase": "Motions",
            },
            {
                "agent": "Defense",
                "text": "Objection — FRE 404(b) prohibits character evidence. The 2018 matter was a documentation error, not a patient safety issue. Introducing it would be highly prejudicial and irrelevant to this case.",
                "phase": "Motions",
            },
            {
                "agent": "Judge",
                "text": "Motion DENIED. The 2018 matter is too dissimilar — a documentation error is not the same as an unauthorized clinical trial. The prejudicial effect substantially outweighs any probative value. FRE 403, 404(b).",
                "phase": "Motions",
            },
            # ════════════════ PHASE 3: OPENING STATEMENTS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to opening statements.", "phase": "Opening"},
            {"agent": "Judge", "text": "Mr. Mercer — the People's opening statement.", "phase": "Opening"},
            {
                "agent": "Prosecutor",
                "text": "Ladies and gentlemen — Marcus Chen was dying of cancer. He came to Northwell Health for treatment, and he put his trust in Dr. Sarah Blake. What he did not know was that Dr. Blake was not following the rules. She gave him an experimental drug that had never been tested in humans. She gave him two and a half times the maximum safe dose. She did not get permission from the ethics committee beforehand — she submitted the paperwork two days AFTER she injected him. And when the patient's mother asked for the consent form, the date had been altered. Marcus Chen died in agony from cytokine storm — his immune system attacking his own organs — because Dr. Blake chose speed over safety. The evidence will show this was not an error — it was criminal recklessness.",
                "phase": "Opening",
            },
            {"agent": "Judge", "text": "Defense counsel.", "phase": "Opening"},
            {
                "agent": "Defense",
                "text": "Members of the jury — Marcus Chen had stage IV metastatic melanoma. He had exhausted every approved treatment. He had weeks to live. Dr. Blake spent hours with him and his family discussing the experimental option. He said — and his family confirms — 'I want to try anything.' Experimental cancer trials are not like taking an aspirin. There are risks. The IRB process has an emergency exception precisely for patients like Marcus who do not have weeks to wait. Dr. Blake followed that exception. The dose she chose was within the range used in similar Phase I trials. And the consent form — dated March 12th — was signed by Marcus Chen himself. The tragedy is that cancer took Marcus Chen. But Dr. Blake did not kill him. She tried to save him.",
                "phase": "Opening",
            },
            # ════════════════ PHASE 4: EVIDENCE PRESENTATION ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to evidence presentation.", "phase": "Evidence"},
            {
                "agent": "Prosecutor",
                "text": "The People submit Exhibit A: the IRB application records showing a submission date of March 15th. Marcus Chen received his first dose on March 13th.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "Objection — the IRB application is a hospital record. It does not reflect the emergency verbal authorization Dr. Blake received from the IRB chair on March 12th under 21 CFR 56.104(c). The written submission is not the whole story.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "The People will call the IRB chair to testify there was no verbal authorization. The written record is the official documentation.",
                "phase": "Evidence",
            },
            {
                "agent": "Judge",
                "text": "Overruled. Exhibit A is admitted as a business record under FRE 803(6). The defense may present evidence of verbal authorization.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "The People submit Exhibit B: the signed consent forms for Marcus Chen. The date line reads March 12th — but the People's forensic document analyst will testify that the '2' in '12' was written over a '3' — meaning the original date was March 13th, altered to appear as March 12th.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "Objection — hearsay and foundation. The consent form is an out-of-court statement offered for the truth of its contents. And the prosecution's document analyst has not been qualified. FRE 1002 — the Best Evidence Rule requires the original document for analysis, and we dispute the chain of custody.",
                "phase": "Evidence",
            },
            {
                "agent": "Judge",
                "text": "Overruled on hearsay — the consent form is not offered for the truth of its contents but as physical evidence of a document. Sustained as to foundation — the exhibit is conditionally admitted pending expert qualification. FRE 104(b). Proceed.",
                "phase": "Evidence",
            },
            {
                "agent": "Prosecutor",
                "text": "The People submit Exhibit C: pharmacy dispensing records showing ONC-279 was prepared and dispensed at 0.75 mg/kg — two and a half times the maximum starting dose of 0.3 mg/kg specified in the IND application.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "No objection, Your Honor. The dose is not in dispute. The dispute is about whether 0.75 mg/kg was appropriate for this patient's condition.",
                "phase": "Evidence",
            },
            {
                "agent": "Judge",
                "text": "Exhibit C admitted.",
                "phase": "Evidence",
            },
            {
                "agent": "Defense",
                "text": "The defense submits Exhibit D: Marcus Chen's medical records documenting stage IV metastatic melanoma with brain metastases, ECOG performance status 3 — indicating he was bedridden more than 50% of the time, with an estimated survival of 4-6 weeks without intervention.",
                "phase": "Evidence",
            },
            {"agent": "Judge", "text": "Exhibit D admitted without objection.", "phase": "Evidence"},
            # ════════════════ PHASE 5: WITNESS EXAMINATION ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to witness examination.", "phase": "Witness"},
            # --- IRB Chair: Dr. Patricia Okonkwo ---
            {
                "agent": "Prosecutor",
                "text": "The People call Dr. Patricia Okonkwo, Chair of the Northwell Health Institutional Review Board. Dr. Okonkwo — did Dr. Blake receive verbal authorization to proceed before March 15th?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "No. There is no record of any verbal authorization. Our standard process requires written submission followed by full committee review. Emergency exceptions under 21 CFR 56.104(c) require documentation within 48 hours — Dr. Blake never provided any.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Had Dr. Blake ever contacted you by phone or email about an emergency exception?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "No. I first learned of this trial when our compliance officer flagged the March 15th application — two days after the patient had already been dosed.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ IRB records reviewed. No emergency exception documentation exists.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Okonkwo — is it possible that Dr. Blake spoke with another IRB committee member or an administrative staffer who verbally indicated the application would be approved?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I am the only person authorized to grant emergency exceptions. No staff member has that authority.",
                "phase": "Witness",
            },
            # --- Forensic Document Analyst ---
            {
                "agent": "Prosecutor",
                "text": "The People call Dr. Karen Sato, forensic document examiner. Dr. Sato — your qualifications?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I hold a Ph.D. in Forensic Document Examination from George Washington University. I have 16 years of experience, am a certified member of the American Board of Forensic Document Examiners, and have testified in 38 federal and state cases involving document authentication and alteration analysis.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "Defense — voir dire?",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Sato — ink dating analysis is not considered reliable by all courts. The Daubert standard requires general acceptance in the scientific community. Has your specific methodology been peer-reviewed?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. My methodology — which combines microscopic examination, infrared spectrometry, and chemical solvent testing — was published in the Journal of Forensic Sciences in 2021 and has been cited in 12 subsequent peer-reviewed studies.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "No further on qualifications.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "The court qualifies Dr. Sato as an expert in forensic document examination under FRE 702. Exhibit B is formally admitted.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Sato — describe your analysis of the consent form.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The date line shows two layers of ink. The underlying digit was written as '3' — consistent with March 13th. A second application of ink converted it to '12' — March 12th. The alteration was made with a pen from a different batch — the ink chemical composition differs from the surrounding text. The signature block was signed at the same time as the altered date, not at the time of the original '3'.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "What does that indicate?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The consent form was originally dated March 13th — the day the dose was administered. The date was later changed to March 12th to make it appear the consent was obtained a day before treatment. The signature was added at the time of the alteration, not at the original signing.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Methodology is peer-reviewed. Findings are documented in expert report.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Sato — your alteration date analysis assumes the document was not handled or exposed to conditions that could affect ink layers. Dr. Blake kept this form in her office for three weeks before producing it. Could normal handling have caused the chemical differences you observed?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Normal handling does not cause chemical composition differences between two ink applications on the same document. The ink batches are chemically distinct — that cannot be explained by handling or environmental exposure.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "And you cannot determine WHO made the alteration, can you? The form could have been altered by anyone in Dr. Blake's office.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I cannot identify the person who made the alteration. I can only identify that an alteration was made.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Sato — one question on redirect. Regardless of who physically altered the document, can you confirm the date was changed from March 13th to March 12th?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. The underlying digit was a '3' — the day of treatment. The altered '12' was applied later. That finding is chemically certain.",
                "phase": "Witness",
            },
            # --- Medical Examiner ---
            {
                "agent": "Prosecutor",
                "text": "The People call Dr. Michael Torres, Chief Medical Examiner for New York County. Dr. Torres — the cause of death for Marcus Chen?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Cytokine storm syndrome — an acute systemic inflammatory response triggered by immune activation. In the context of this case, it was caused by the administration of ONC-279 at 0.75 mg/kg. The massive release of cytokines led to multiorgan failure including acute respiratory distress syndrome, acute kidney injury, and hepatic failure. Mr. Chen died approximately 72 hours after infusion.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "In your expert opinion, was the dose a substantial factor in causing death?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Unequivocally yes. The probability of cytokine storm at the approved starting dose of 0.3 mg/kg is approximately 3-5%. At 0.75 mg/kg, the probability increases to approximately 40-60%. The dose escalation was the proximate cause of the fatal reaction.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Dosing probability data sourced from IND application and published Phase I safety data.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Torres — you cited the IND application data. But the IND data is for patients with solid tumors who have not exhausted treatment options. Mr. Chen had stage IV disease with brain metastases and ECOG 3. There is no published safety data for that population. The 40-60% probability you cite is an extrapolation, not a known fact — correct?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The probability range is an extrapolation based on the known dose-response relationship of ONC-279. No Phase I trial has been conducted specifically in ECOG 3 patients — that is true. The extrapolation is medically reasonable.",
                "phase": "Witness",
            },
            # --- Blake's Defense Expert: Dr. Jonathan Weiss ---
            {
                "agent": "Defense",
                "text": "The defense calls Dr. Jonathan Weiss, Professor of Clinical Pharmacology at Columbia University. Dr. Weiss — your qualifications?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I hold an M.D. and Ph.D. in Pharmacology from Johns Hopkins. I have 22 years of experience in oncology drug development, have served as principal investigator on 14 Phase I trials, and have published over 60 papers on dose-finding methodology in oncology. I currently serve on the FDA's Oncologic Drugs Advisory Committee.",
                "phase": "Witness",
            },
            {
                "agent": "Judge",
                "text": "Prosecution — voir dire?",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Weiss — you serve on the FDA advisory committee that evaluates oncology drugs. You also consult for pharmaceutical companies developing those same drugs. Is that not a conflict of interest?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I recuse myself from any FDA decision involving companies I consult for. My advisory role is separate from my consulting work. All conflicts are disclosed.",
                "phase": "Witness",
            },
            {"agent": "Prosecutor", "text": "No further on qualifications.", "phase": "Witness"},
            {
                "agent": "Judge",
                "text": "The court qualifies Dr. Weiss as an expert in clinical pharmacology under FRE 702.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Dr. Weiss — in your opinion, was 0.75 mg/kg a reasonable dose for Marcus Chen given his condition?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. In Phase I oncology trials, dose escalation is guided by the patient's condition. For a patient with weeks to live, the risk-benefit calculus shifts. The standard 3+3 dose escalation design starts at 0.3 mg/kg in fit patients. For a moribund patient, many investigators would consider up to 1.0 mg/kg justified. Dr. Blake's choice of 0.75 mg/kg was within the range of reasonable medical judgment.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Did Dr. Blake have a duty to wait for full IRB approval before administering the drug?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "The regulations at 21 CFR 56.104(c) permit emergency use without prior IRB approval when the patient's life is at immediate risk and no alternative exists. Mr. Chen had no remaining standard treatment options. An argument can be made that this fell within the emergency exception — even if the paperwork was not perfectly completed.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Expert offered opinion on standard of care. Jury may weigh credibility.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Weiss — you said the dose was within reasonable medical judgment. But the IND application clearly states 0.3 mg/kg as the maximum safe starting dose. Dr. Blake exceeded that by 150%. Does the term 'maximum safe starting dose' leave room for a 150% deviation?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "IND applications state conservative starting doses designed for the general clinical trial population. In specific clinical circumstances, the investigator has discretion to adjust. This is standard practice in oncology.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "And the backdated consent form — is it 'standard practice' to alter a patient's consent date?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I do not know who altered that form. I am not testifying about the consent form. I am testifying about the dosing decision.",
                "phase": "Witness",
            },
            # --- Dr. Sarah Blake (defendant testimony) ---
            {
                "agent": "Defense",
                "text": "The defense calls Dr. Sarah Blake. Dr. Blake — describe your relationship with Marcus Chen.",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Marcus was my patient for eight months. I treated him through two lines of chemotherapy, immunotherapy, and radiation. When everything failed, I discussed the ONC-279 trial with him. I was transparent — I told him it had never been tested in humans, that the risks included possible death, and that it was unlikely to work. He said he wanted to try. He said 'I'm not afraid of the risk — I'm afraid of not trying.' I believed I was giving him a chance.",
                "phase": "Witness",
            },
            {
                "agent": "Defense",
                "text": "Why did you administer the dose before receiving written IRB approval?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "His condition was deteriorating rapidly. He developed new brain metastases on March 10th. The standard IRB process takes 4-6 weeks. He did not have 4-6 weeks. I believed the emergency exception applied. I take full responsibility for the decision — but I made it in his best interest.",
                "phase": "Witness",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ Medical records confirm rapid deterioration in early March.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "Dr. Blake — the consent form. Who altered the date from March 13th to March 12th?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I did not alter the date. I reviewed the form with Marcus on March 12th. We discussed it for about 45 minutes. He signed it. I do not know why the forensic analyst found two ink layers. I did not change it.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "But the analyst testified that the ink from the '12' is chemically different from the surrounding text. How do you explain that?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "I cannot explain it. I used the pen on my desk — perhaps the pen has two ink cartridges. I am not a document examiner. I only know I did not alter any date.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "You emailed a colleague saying 'We can submit the IRB retroactively.' Those are your words, correct?",
                "phase": "Witness",
            },
            {
                "agent": "Witness",
                "text": "Yes. I wrote that. But 'retroactively' referred to the modification process under the emergency exception. I was expressing confidence that our IRB would approve the retrospective documentation. I was not describing a plan to deceive.",
                "phase": "Witness",
            },
            {
                "agent": "Prosecutor",
                "text": "No further questions.",
                "phase": "Witness",
            },
            # ════════════════ PHASE 6: REBUTTAL EVIDENCE ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to rebuttal evidence.", "phase": "Rebuttal"},
            {"agent": "Judge", "text": "Prosecution — rebuttal?", "phase": "Rebuttal"},
            {
                "agent": "Prosecutor",
                "text": "The defense asks you to believe in the 'emergency exception.' But the IRB chair — Dr. Okonkwo — testified there was no verbal authorization. The defense claims the dose was appropriate — but the IND application says 0.3 mg/kg is the maximum safe starting dose. Dr. Weiss, the defense's own expert, admitted he was not testifying about the consent form — because he cannot explain it. The altered date. The unauthorized trial. The fatal dose. Three separate failures. Each one, on its own, is a deviation from the standard of care. Together, they constitute criminal negligence.",
                "phase": "Rebuttal",
            },
            {"agent": "Judge", "text": "Defense — surrebuttal?", "phase": "Rebuttal"},
            {
                "agent": "Defense",
                "text": "The prosecution conflates paperwork errors with criminal intent. Dr. Blake spent 45 minutes with Marcus Chen explaining the risks. The form was signed. The emergency exception exists for patients exactly like Marcus — dying patients with no options. The dose was within the range Dr. Weiss — an FDA advisor — considers reasonable. The prosecution has not proven beyond reasonable doubt that Dr. Blake acted with criminal recklessness. They have proven she filled out paperwork imperfectly while trying to save a dying man's life. That is not manslaughter.",
                "phase": "Rebuttal",
            },
            {
                "agent": "Fact Checker",
                "text": "✓ All evidence and testimony noted. Jury to determine criminal intent.",
                "phase": "Rebuttal",
            },
            # ════════════════ PHASE 7: CLOSING ARGUMENTS ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to closing arguments.", "phase": "Closing"},
            {
                "agent": "Prosecutor",
                "text": "Ladies and gentlemen — this case comes down to three things. One: the IRB application was submitted after the dose was given — not before. Two: the consent form date was altered — changed from the day of treatment to the day before. Three: the dose was two and a half times the maximum safe starting dose — a dose that increased the risk of death tenfold. Dr. Blake says she was trying to save a life. But the rules exist to protect patients like Marcus Chen. The IRB process exists to ensure experimental treatments are safe. The dose limits exist for a reason. Dr. Blake bypassed every safeguard. Marcus Chen died as a result. That is not good medicine — that is criminal recklessness. The People ask you to return a verdict of Guilty.",
                "phase": "Closing",
            },
            {
                "agent": "Defense",
                "text": "Dr. Sarah Blake is not a criminal. She is a doctor who spent 15 years treating the sickest patients. When Marcus Chen was dying, with no options left, she offered him hope. She discussed the risks. He consented. She used a dose within the range that an FDA advisory committee member considers acceptable. The paperwork — yes, it was imperfect. But paperwork errors are not manslaughter. The prosecution has not proven beyond reasonable doubt that Dr. Blake acted with criminal intent. If you have any doubt — any doubt at all — about whether Sarah Blake knowingly caused Marcus Chen's death, you must find her Not Guilty.",
                "phase": "Closing",
            },
            # ════════════════ PHASE 8: JURY INSTRUCTIONS ════════════════
            {
                "agent": "Bailiff",
                "text": "The court will now proceed to jury instructions.",
                "phase": "Jury Instructions",
            },
            {
                "agent": "Judge",
                "text": "Members of the jury — Count One charges the defendant with Involuntary Manslaughter under 18 U.S.C. § 1112. To find the defendant guilty, the prosecution must prove beyond a reasonable doubt: (1) the defendant acted with criminal negligence — meaning a gross deviation from the standard of care that a reasonable person would observe in the same situation; (2) the defendant's actions caused the death of Marcus Chen; and (3) the defendant did not act with lawful authority or justification. Count Two charges Reckless Endangerment under New York Penal Law 120.25 — recklessly engaging in conduct that created a substantial risk of serious physical injury to another person. The defendant is presumed innocent. If you have a reasonable doubt, you must acquit.",
                "phase": "Jury Instructions",
            },
            # ════════════════ PHASE 9: JURY DELIBERATION ════════════════
            {
                "agent": "Bailiff",
                "text": "The court will now proceed to jury deliberation.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Let us begin. Please state your initial positions on the manslaughter count.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #1 (Analytical): Guilty. The consent form alteration is the key piece of evidence. If everything was above board, there would be no need to change the date. That shows consciousness of guilt.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #2 (Empathetic): Not Guilty. I believe Dr. Blake was trying to help. The patient was dying. She gave him a chance. The paperwork was messy but her intent was not criminal.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #3 (Skeptical): Guilty. The dose was 2.5x the safe starting dose. The IRB was not informed. The consent form was altered. Even if she meant well, her actions were grossly negligent. Good intentions do not negate recklessness.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #4 (Pragmatic): Guilty. Three separate protocol violations — any one might be an error. Three together is a pattern. The ethical rules exist for a reason. She ignored them and a patient died.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Round 1: 3 Guilty, 1 Not Guilty. Juror #2 — what would change your mind?",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Juror",
                "text": "Juror #2: I keep thinking about the patient's family. They said he wanted to try anything. But the dose issue — 2.5 times the safe dose — that is hard to explain. And the altered date... I cannot reconcile that with good intent. I change my vote to Guilty.",
                "phase": "Jury Deliberation",
            },
            {
                "agent": "Foreperson",
                "text": "Round 2: 4 Guilty, 0 Not Guilty. Unanimous verdict reached on Count One.",
                "phase": "Jury Deliberation",
            },
            # ════════════════ PHASE 10: SHADOW JURY ════════════════
            {"agent": "Bailiff", "text": "The shadow jury has convened for analysis.", "phase": "Shadow Jury"},
            {
                "agent": "Juror",
                "text": "Shadow Juror 1 (Liam): The altered consent form is the most damning evidence. If the date was legitimate, why change it? That single act undermines the entire defense. [Vote: Guilty, confidence 85%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 2 (Sarah): The dose argument cuts both ways. Dr. Weiss made a reasonable case for clinical discretion. But the combination of no IRB approval + altered consent + excessive dosing creates a pattern of recklessness. [Vote: Guilty, confidence 72%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 3 (Marcus): Dr. Blake's motive was to help — I accept that. But motive is not a defense. The rules exist for patient safety. She knowingly bypassed them. The result was foreseeable. [Vote: Guilty, confidence 78%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 4 (Elena): The prosecution proved that the consent form was altered. Dr. Blake's explanation — a pen with two ink cartridges — is not credible. If she lied about that, what else is she lying about? [Vote: Guilty, confidence 81%]",
                "phase": "Shadow Jury",
            },
            {
                "agent": "Juror",
                "text": "Shadow Juror 5 (David): I struggle with this. She was trying to save a dying man. But the law requires following safety protocols, especially with experimental treatments. The deviation was too extreme. [Vote: Guilty, confidence 68%]",
                "phase": "Shadow Jury",
            },
            {"agent": "Bailiff", "text": "The shadow jury has completed its analysis.", "phase": "Shadow Jury"},
            # ════════════════ PHASE 11: SENTENCING ════════════════
            {"agent": "Bailiff", "text": "The court will now proceed to sentencing.", "phase": "Sentencing"},
            {
                "agent": "Judge",
                "text": "The jury has returned a verdict of Guilty on Count One — Involuntary Manslaughter — and Count Two — Reckless Endangerment. We now proceed to sentencing. Mr. Mercer — the People may address the court on aggravation.",
                "phase": "Sentencing",
            },
            {
                "agent": "Prosecutor",
                "text": "Your Honor, the People request a sentence of 8 to 12 years. Dr. Blake abused her position of trust as a physician. She conducted an unauthorized experiment on a vulnerable patient who had no reason to doubt that his doctor was following the rules. She altered the consent form — a deliberate act to conceal her deviation from protocol. The victim's mother testified at trial that she trusted Dr. Blake completely. That trust was betrayed. The sentence must reflect the gravity of a death caused by a physician's criminal negligence.",
                "phase": "Sentencing",
            },
            {
                "agent": "Judge",
                "text": "Defense counsel — mitigation?",
                "phase": "Sentencing",
            },
            {
                "agent": "Defense",
                "text": "Your Honor, Dr. Blake has dedicated 15 years to treating the most difficult cancer cases. Hundreds of patients are alive because of her care. She has no prior criminal record. The evidence showed she spent 45 minutes discussing risks with Marcus Chen — she did not act with malice. She acted out of compassion for a dying man. She will lose her medical license as a result of these proceedings — that alone is a severe punishment. We ask the court to impose the minimum sentence of 3 years, with eligibility for probation, and to consider that her 12-year-old daughter will be without a mother if she is incarcerated.",
                "phase": "Sentencing",
            },
            {
                "agent": "Judge",
                "text": "Dr. Sarah Blake — please rise. The evidence at trial established beyond reasonable doubt that you conducted an unauthorized clinical trial, administered a fatal dose of an experimental drug, and altered a consent form to conceal your actions. Marcus Chen trusted you, and you violated that trust. However, this court also considers your 15 years of service to critically ill patients, your lack of prior criminal history, and the extensive character testimony from your colleagues. The court hereby sentences you as follows: On Count One — Involuntary Manslaughter — 6 years of imprisonment. On Count Two — Reckless Endangerment — 3 years, to be served concurrently with Count One. You are remanded to the custody of the Federal Bureau of Prisons. Your medical license shall be referred to the New York State Medical Board for revocation proceedings. This court is adjourned.",
                "phase": "Sentencing",
            },
            # ════════════════ PHASE 12: COURT REPORTER ════════════════
            {
                "agent": "Bailiff",
                "text": "Case 24-CR-0211 — State of New York versus Dr. Sarah Blake — is concluded. The trial record shall be certified by the court reporter.",
                "phase": "Court Reporter Log",
            },
            {
                "agent": "System",
                "text": "[Court Reporter Log: Complete trial record compiled. Case 24-CR-0211. Verdict: GUILTY on all counts. Sentence: 6 years imprisonment. Transcript includes 4 exhibits, 6 witnesses including 2 expert qualifications, 3 objections with rulings, 2 pre-trial motions, 4-phase adversarial process, 5 shadow juror analyses, full sentencing hearing.]",
                "phase": "Court Reporter Log",
            },
            # ════════════════ ADJOURNED ════════════════
            {
                "agent": "Bailiff",
                "text": "All charges have been adjudicated. This court is adjourned.",
                "phase": "Adjourned",
            },
        ],
        "verdict": "GUILTY",
        "win_probability": 0.71,
        "sensitivity": "If consent forms were properly dated and signed before treatment → Defense win probability rises to 65%",
        "sentence": {
            "sentence": "On Count One — Involuntary Manslaughter — 6 years imprisonment. On Count Two — Reckless Endangerment — 3 years, concurrent.",
            "term": "6 years imprisonment. Eligibility for parole after serving 85% of sentence.",
            "rationale": "Aggravating factors: abuse of physician trust, altered consent form, 2.5x maximum safe dose, death of patient. Mitigating factors: 15 years of patient care, no prior criminal record, patient's terminal condition and consent, character references from colleagues, impact on dependent child.",
        },
        "shadow_jury_narrative": [
            {
                "name": "Shadow Juror 1",
                "content": "The altered consent form is the most damning evidence. If the date was legitimate, why change it? That single act undermines the entire defense. [Vote: Guilty]",
            },
            {
                "name": "Shadow Juror 2",
                "content": "The dose argument cuts both ways. But the combination of no IRB approval + altered consent + excessive dosing creates a pattern of recklessness. [Vote: Guilty]",
            },
            {
                "name": "Shadow Juror 3",
                "content": "Dr. Blake's motive was to help — I accept that. But motive is not a defense. The rules exist for patient safety. She knowingly bypassed them. [Vote: Guilty]",
            },
            {
                "name": "Shadow Juror 4",
                "content": "The prosecution proved the consent form was altered. Dr. Blake's explanation — a pen with two ink cartridges — is not credible. [Vote: Guilty]",
            },
            {
                "name": "Shadow Juror 5",
                "content": "She was trying to save a dying man. But the law requires following safety protocols for experimental treatments. The deviation was too extreme. [Vote: Guilty]",
            },
        ],
    },
}
