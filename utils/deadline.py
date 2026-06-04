def get_upcoming_deadlines(exam_name: str = "") -> str:
    deadlines = {
        "SSC CGL": {
            "notification": "August 2026",
            "application_start": "August 2026",
            "application_end": "September 2026",
            "exam_date": "December 2026",
            "website": "ssc.gov.in"
        },
        "SSC CHSL": {
            "notification": "June 2026",
            "application_start": "June 2026",
            "application_end": "July 2026",
            "exam_date": "October 2026",
            "website": "ssc.gov.in"
        },
        "UPSC CSE": {
            "notification": "February 2026",
            "application_start": "February 2026",
            "application_end": "March 2026",
            "exam_date": "May 2026",
            "website": "upsc.gov.in"
        },
        "RRB NTPC": {
            "notification": "Expected late 2026",
            "application_start": "TBA",
            "application_end": "TBA",
            "exam_date": "TBA",
            "website": "indianrailways.gov.in"
        },
        "IBPS PO": {
            "notification": "July 2026",
            "application_start": "July 2026",
            "application_end": "August 2026",
            "exam_date": "October 2026",
            "website": "ibps.in"
        },
        "MPSC": {
            "notification": "June 2026",
            "application_start": "June 2026",
            "application_end": "July 2026",
            "exam_date": "September 2026",
            "website": "mpsc.gov.in"
        }
    }

    note = "\n⚠️  Always verify exact dates on official websites before applying.\n"

    if exam_name and exam_name != "All":
        exam_upper = exam_name.upper()
        for key, value in deadlines.items():
            if exam_upper in key.upper() or key.upper() in exam_upper:
                result  = f"📅 {key} — Upcoming Dates\n"
                result += f"{'─'*35}\n"
                result += f"  Notification    : {value['notification']}\n"
                result += f"  Application     : {value['application_start']} – {value['application_end']}\n"
                result += f"  Exam Date       : {value['exam_date']}\n"
                result += f"  Official Website: {value['website']}\n"
                result += note
                return result
        return f"⚠️  No deadline info found for '{exam_name}'. Please check the official website."

    result = "📅 Upcoming Exam Deadlines — 2026\n"
    result += f"{'═'*40}\n\n"
    for exam, info in deadlines.items():
        result += f"🔹 {exam}\n"
        result += f"   Application : {info['application_end']}\n"
        result += f"   Exam Date   : {info['exam_date']}\n"
        result += f"   Website     : {info['website']}\n\n"
    result += note
    return result