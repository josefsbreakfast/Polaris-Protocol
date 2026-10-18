class ExPMZoltarMachine:
    """
    🔮 SPECIAL EX-PM ZOLTAR MACHINE DETECTOR
    Polaris Protocol | 👑 The Worst Three Kings

    Purpose:
        Detect suspicious concentrations of former
        prime ministers in places where nobody
        specifically invited them.
    """

    def scan(self, document):

        print("🔮 INSERT DECLASSIFIED DOCUMENT")
        print("⚙️ WHIRRRRRRR...")
        print("⚙️ CLUNK.")
        print("👑 FORMER PRIME MINISTER DETECTED.")

        if "Tony Blair" in document:
            print("🚨 OH FOR FUCK'S SAKE.")
            print("🇬🇧 IT'S TONY BLAIR AGAIN.")
            print("📋 Checking diplomatic remit...")
            print("📋 Checking consultancy arrangements...")
            print("📋 Checking why he's even here...")

            raise Exception(
                "ERROR 2007: "
                "TONY BLAIR HAS NEVER ACTUALLY LEFT."
            )

        return "Further former prime ministers pending review."


# 🦅 Polaris investigative methodology

zoltar = ExPMZoltarMachine()

try:
    zoltar.scan("Epstein DOJ files: Tony Blair")
except Exception as e:
    print(e)
    print("🙄 PUT HIM BACK IN THE FILING CABINET.")
    print("👑 AND CHECK FOR ANY OTHERS.")
