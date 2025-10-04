# Classroom Scheduling Algorithm

# ------------------ BASIC CONSTANTS ------------------
PROGRAMS = ["BSIT", "BSIS", "BSCS"]
YEARS = [1, 2, 3, 4]
SECTION_CAPACITY = 40

# ------------------ MAKE SECTIONS ------------------
def make_sections(populations, capacity=SECTION_CAPACITY):
    # populations: {'BSIT':[y1,y2,y3,y4], ...}
    letters = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
    sections_map = {}
    for prog in PROGRAMS:
        year_list = populations.get(prog, [0, 0, 0, 0])
        sections_map[prog] = {}
        for year_number, pop in enumerate(year_list, start=1):
            year_sections = []
            if pop > 0:
                need = (pop + capacity - 1) // capacity
                for i in range(need):
                    year_sections.append(f"{prog}{year_number}{letters[i]}")
            sections_map[prog][year_number] = year_sections
    return sections_map

# ------------------ HARDCODED COURSE TABLES (Code, Title, LecHrs, LabHrs) ------------------

# BSIT — Year 1
BSITterm1_year1 = [
    ["INTCOMC", "INTRODUCTION TO COMPUTING FOR CS / IT", 2, 2],
    ["PROGCON", "Programming Concepts and Logic", 2, 2],
    ["COMPORG", "COMPUTER ORGANIZATION & ARCHITECTURE", 2, 2],
]

BSITterm2_year1 = [
    ["INPROLA", "INTRODUCTION TO PROGRAMMING & THEORIES", 2, 2],
    ["MANPRIN", "MANAGEMENT PRINCIPLES", 4, 0],
    ["OPESYST", "OPERATING SYSTEMS", 2, 2],
]

BSITterm3_year1 = [
    ["DASTRUC", "DATA STRUCTURES", 2, 2],
    ["BUSPROS", "Business Process", 4, 0],
    ["DNETCOM", "NETWORK SECURITY, STORAGE & DATA COMMUNICATION", 2, 2],
]

# BSIT — Year 2
BSITterm1_year2 = [
    ["USERDES", "UI/UX DESIGN AND PROGRAMMING", 2, 2],
    ["DISCRET", "DISCRETE MATH", 4, 0],
    ["DATAMA1", "DATABASE MANAGEMENT 1", 2, 2],
    ["QUAMET1", "QUANTITATIVE METHODS 1", 2, 2],
    ["RPASYST", "RPA SYSTEMS", 2, 2],
    ["INFOSEC", "INFORMATION SECURITY", 2, 2],
]

BSITterm2_year2 = [
    ["WEBPROG", "WEB PROGAMMING (for BSIT)", 2, 2],
    ["MOBPROG", "MOBILE PROGRAMMING", 2, 2],
    ["DATAMA2", "DATABASE MANAGEMENT 2 and ADMINISTRATION", 2, 2],
    ["PEMBEDS", "PROGRAMMING EMBEDDED SYSTEMS", 2, 2],
    ["ELECTV1", "ELECTIVE 1", 2, 2],
    ["CLDCOMP", "CLOUD COMPUTING & VIRTUALIZATION", 2, 2],
]

BSITterm3_year2 = [
    ["EXCOMP1", "EXTENSIVE COMPETENCY COMMUNICATION PROGRAM 1", 2, 2],
    ["MNTSDEV", "INTRODUCTION TO SYSTEMS AND DESIGN", 2, 2],
    ["ELECTV2", "ELECTIVE 2", 2, 2],
]

# BSIT — Year 3
BSITterm1_year3 = [
    ["MSYADD1", "SYSTEMS ANALYSIS & DETAILED DESIGN", 2, 2],
    ["ELECTV3", "ELECTIVE 3", 2, 2],
    ["ICTSRV1", "ICT SERVICES MANAGEMENT (A+ PC TROUBLESHOOTING)", 2, 2],
]

BSITterm2_year3 = [
    ["MCSPROJ", "APPLIED PROJECT - SYSTEM PHOTOTYPE", 2, 2],
    ["TENTREP", "TECHNOPRENEURSHIP", 4, 0],
    ["ELECTV4", "ELECTIVE 4", 2, 2],
]

BSITterm3_year3 = [
    ["PROJMAN", "PROJECT MANAGEMENT", 2, 2],
    ["MNSYSIT", "MANAGEMENT INFORMATION SYSTEMS & IT TRENDS", 2, 2],
    ["ITBLAWS", "IT AND BUSINESS LAWS", 4, 0],
]

# BSIT — Year 
BSITterm1_year4 = [
    ["PROFETH", "PROFESSIONAL ETHICS", 4, 0],
    ["SOFTDEV", "SOFTWARE DEVELOPMENT", 2, 2],
    ["QUALITY", "SOFTWARE QUALITY MANAGEMENT", 2, 2],
]

BSITterm2_year4 = [
    ["xINTERN1", "INTERNSHIP 1", 4, 0],
]

BSITterm3_year4 = [
    ["INTERN2", "INTERNSHIP 2", 4, 0],
]


# BSIS — Year 1
BSISterm1_year1 = [
    ["CCINCOMX", "INTRODUCTION TO COMPUTING - LEC", 2.66, 0],
    ["CCINCOBL", "INTRODUCTION TO COMPUTING - LAB", 0, 4],
    ["CCPRGG1X", "FUNDAMENTALS OF PROGRAMMING - LEC", 2.66, 0],
    ["CCPRG1BL", "FUNDAMENTALS OF PROGRAMMING - LAB", 0, 4],
]

BSISterm2_year1 = [
    ["CCFUINSY", "FUNDAMENTALS OF INFORMATION SYSTEMS", 2.66, 4],
    ["CCPRGG2X", "INTERMEDIATE PROGRAMMING - LEC", 2.66, 0],
    ["CCPRG2BL", "INTERMEDIATE PROGRAMMING - LAB", 0, 4],
]

BSISterm3_year1 = [
    ["CCDATRCL", "DATA STRUCTURES AND ALGORITHMS", 2.66, 4],
    ["CCORMACO", "ORGANIZATION AND MANAGEMENT CONCEPTS", 2.66, 4],
]

# BSIS — Year 2
BSISterm1_year2 = [
    ["CTINFMGL", "INFORMATION MANAGEMENT", 2.66, 4],
    ["CCSPEL1X", "SPORTS ELECTIVE 1 ( E-GAMES DESIGN I )", 2, 2],
]

BSISterm2_year2 = [
    ["CIENTARL", "ENTERPRISE ARCHITECTURE", 2.66, 4],
    ["CCSPEL2X", "SPORTS ELECTIVE 2 ( E- GAMES DESIGN II )", 2, 2],
    ["CCQUAMET", "QUANTITATIVE METHODS", 2.66, 4],
    ["BUPRDEMA", "BUSINESS PROCESS MANAGEMENT", 4, 0],
]

BSISterm3_year2 = [
    ["ITINNETE", "I.T. INFRASTRUCTURE AND NETWORK TECHNOLOGIES", 2.66, 4],
    ["CCDATSYL", "DATABASE SYSTEMS", 2.66, 4],
]

# BSIS — Year 3
BSISterm1_year3 = [
    ["BAFINMAX", "FINANCIAL MANAGEMENT", 4, 0],
    ["CIEVBUPE", "EVALUATION OF BUSINESS PERFORMANCE", 4, 0],
    ["CIMUCOGL", "MULTIMEDIA AND COMPUTER GRAPHICS", 2.66, 4],
    ["CIWEBPRL", "WEB PROGRAMMING", 2.66, 4],
]

BSISterm2_year3 = [
    ["CISECDEL", "E-COMMERCE AND DIGITAL ENTREPRENEURSHIP", 4, 0],
    ["CTSYSADL", "SYSTEMS ANALYSIS AND DESIGN", 2.66, 4],
    ["CISPRMAL", "I.S. PROJECT MANAGEMENT", 2.66, 4],
    ["CISELE1L", "I.S. ELECTIVE 1", 2.66, 4],
]

BSISterm3_year3 = [
    ["CTAPDEVL", "APPLICATION DEVELOPMENT AND EMERGING TECHNOLOGY", 2.66, 4],
    ["CCSFEN1L", "SOFTWARE ENGINEERING 1", 2.66, 4],
    ["CISELE2L", "I.S. ELECTIVE 2", 2.66, 4],
]

# BSIS — Year 4
BSISterm1_year4 = [
    ["CAPROJ1L", "CAPSTONE PROJECT 1", 2.66, 4],
    ["ISSTMAAC", "I.S. STRATEGY MANAGEMENT AND ACQUISITION", 2.66, 4],
    ["CISELE3L", "I.S. ELECTIVE 3", 2.66, 4],
]

BSISterm2_year4 = [
    ["CCISINTX", "INTERNSHIP (486 HRS)", 4, 0],
]

BSISterm3_year4 = [
    ["CAPROJ2L", "CAPSTONE PROJECT 2", 2.66, 4],
    ["PRISINSY", "PROFESSIONAL ISSUES IN INFORMATION SYSTEMS", 4, 0],
    ["CISELE4L", "I.S. ELECTIVE 4", 2.66, 4],
]

# BSCS — Year 1
BSCSterm1_year1 = [
    ["CCINCOMX", "INTRODUCTION TO COMPUTING - LEC", 2.66, 0],
    ["CCINCOBL", "INTRODUCTION TO COMPUTING - LAB", 0, 4],
    ["CCPRGG1X", "FUNDAMENTALS OF PROGRAMMING - LEC", 2.66, 0],
    ["CCPRG1BL", "FUNDAMENTALS OF PROGRAMMING - LAB", 0, 4],
]

BSCSterm2_year1 = [
    ["CCDISTR1", "DISCRETE STRUCTURES 1", 2.66, 4],
    ["CCPRGG2X", "INTERMEDIATE PROGRAMMING - LEC", 2.66, 0],
    ["CCPRG2BL", "INTERMEDIATE PROGRAMMING - LAB", 0, 4],
]

BSCSterm3_year1 = [
    ["CCDISTR2", "DISCRETE STRUCTURES 2", 2.66, 4],
    ["CCOBJPGL", "OBJECT-ORIENTED PROGRAMMING", 0, 4],
    ["CCOBJPGX", "OBJECT-ORIENTED PROGRAMMING - LEC", 2.66, 0],
]

# BSCS — Year 2
BSCSterm1_year2 = [
    ["CTINFMGL", "INFORMATION MANAGEMENT", 2.66, 4],
    ["CCDATRCL", "DATA STRUCTURES AND ALGORITHMS", 2.66, 4],
    ["CCSPEL1X", "SPORTS ELECTIVE 1 ( E-GAMES DESIGN I )", 2, 1],
]

BSCSterm2_year2 = [
    ["CCOMPORL", "COMPUTER ARCHITECTURE AND ORGANIZATION", 2.66, 4],
    ["CCDATSYL", "DATABASE SYSTEMS", 2.66, 4],
    ["CCSPEL2X", "SPORTS ELECTIVE 2 ( E- GAMES DESIGN II )", 2, 2],
]

BSCSterm3_year2 = [
    ["CCQUAMET", "QUANTITATIVE METHODS", 2.66, 4],
    ["CCOPSYSL", "OPERATING SYSTEMS", 2.66, 4],
]

# BSCS — Year 3
BSCSterm1_year3 = [
    ["CCALCOML", "ALGORITHMS AND COMPLEXITY", 2.66, 4],
    ["CIWEBPRL", "WEB PROGRAMMING", 2.66, 4],
    ["CCHUCOIL", "HUMAN-COMPUTER INTERACTION", 2.66, 4],
    ["CIMUCOGL", "MULTIMEDIA AND COMPUTER GRAPHICS", 2.66, 4],
]

BSCSterm2_year3 = [
    ["CCSFEN1L", "SOFTWARE ENGINEERING 1", 2.66, 4],
    ["CTINASSL", "INFORMATION ASSURANCE AND SECURITY", 2.66, 4],
    ["CCNETCOL", "NETWORK AND COMMUNICATIONS", 2.66, 4],
]

BSCSterm3_year3 = [
    ["CCAUTOMA", "AUTOMATA THEORY AND FORMAL LANGUAGES", 2.66, 4],
    ["CTAPDEVL", "APPLICATION DEVELOPMENT AND EMERGING TECHNOLOGY", 2.66, 4],
    ["CCSFEN2L", "SOFTWARE ENGINEERING 2", 2.66, 4],
]

# BSCS — Year 4
BSCSterm1_year4 = [
    ["CCTHES1L", "THESIS 1", 2.66, 4],
    ["CCPGLANL", "PROGRAMMING LANGUAGES", 2.66, 4],
    ["CCSELE1L", "C.S. ELECTIVE 1", 2.66, 4],
]

BSCSterm2_year4 = [
    ["CCCSINTX", "INTERNSHIP (MIN. 162 HRS)", 0, 4],
    ["CCSELE2L", "C.S. ELECTIVE 2", 2.66, 4],
]

BSCSterm3_year4 = [
    ["CCTHES2L", "THESIS 2", 2.66, 4],
    ["CCSELE3L", "C.S. ELECTIVE 3", 2.66, 4],
    ["CTPRFISS", "SOCIAL AND PROFESSIONAL ISSUES", 4, 0],
]

# ------------------ HELPERS TO CONVERT TABLE ROWS TO COURSE DICTS ------------------
def _to_minutes(val):
    if val is None:
        return 0
    s = str(val).strip()
    if s == "":
        return 0
    try:
        return int(round(float(s) * 60))
    except Exception:
        return 0

def add_courses_from_table(program, term, year, table_rows, out_list):
    for row in table_rows:
        if not isinstance(row, (list, tuple)) or len(row) < 1:
            continue
        code = str(row[0]).strip()
        lec = row[2] if len(row) > 2 else ""
        lab = row[3] if len(row) > 3 else ""
        if code == "":
            continue
        out_list.append({
            "program": program,
            "year": int(year),
            "term": int(term),
            "code": code,
            "lec_minutes": _to_minutes(lec),
            "lab_minutes": _to_minutes(lab),
        })

# ------------------ MAIN ------------------
def main():
    import argparse, csv
    parser = argparse.ArgumentParser(description="Classroom scheduling (demo mode loads sample populations)")
    parser.add_argument('--demo', action='store_true', help='Run in demo mode with sample populations and no interactive input')
    parser.add_argument('--export-csv', action='store_true', help='Export generated schedules to CSV files (term1.csv, term2.csv, term3.csv)')
    args = parser.parse_args()

    print("=== Enrollment Input ===")
    populations = {}
    if args.demo:
        populations = {
            'BSIT': [80, 60, 40, 20],
            'BSIS': [50, 30, 20, 10],
            'BSCS': [70, 50, 30, 10],
        }
        print("Running in demo mode. Populations:")
        for prog, yrs in populations.items():
            print(f"  {prog}: {yrs}")
    else:
        for prog in PROGRAMS:
            print("\nEnter enrollment for", prog)
            year_list = []
            for y in YEARS:
                while True:
                    try:
                        val = int(input(f"  Year {y} population (0 if none): "))
                        if val < 0:
                            print("    Must be >= 0.")
                            continue
                        year_list.append(val)
                        break
                    except ValueError:
                        print("    Invalid number.")
            populations[prog] = year_list

    sections_map = make_sections(populations, capacity=SECTION_CAPACITY)

    print("\nSections Created (with totals):")
    total_sections_all = 0
    total_slots_all = 0
    for prog in PROGRAMS:
        print("\n" + prog + ":")
        prog_sec_total = 0
        prog_slot_total = 0
        for y in YEARS:
            secs = sections_map[prog].get(y, [])
            n = len(secs)
            slots = n * SECTION_CAPACITY
            prog_sec_total += n
            prog_slot_total += slots
            if n == 0:
                print(f"  Year {y}: (none)")
            else:
                print(f"  Year {y}: {', '.join(secs)}")
        print(f"  TOTAL {prog}: Sections={prog_sec_total} Slots={prog_slot_total}")
        total_sections_all += prog_sec_total
        total_slots_all += prog_slot_total
    print(f"\nOVERALL TOTAL: Sections={total_sections_all} Slots={total_slots_all}")

    # ------------------ BUILD COURSES LISTS FROM HARDCODED TABLES (TERMS 1,2,3) ------------------
    courses_term1 = []
    courses_term2 = []
    courses_term3 = []

    def add_all_terms():
        # BSIT
        add_courses_from_table("BSIT", 1, 1, BSITterm1_year1, courses_term1)
        add_courses_from_table("BSIT", 1, 2, BSITterm1_year2, courses_term1)
        add_courses_from_table("BSIT", 1, 3, BSITterm1_year3, courses_term1)
        add_courses_from_table("BSIT", 1, 4, BSITterm1_year4, courses_term1)

        add_courses_from_table("BSIT", 2, 1, BSITterm2_year1, courses_term2)
        add_courses_from_table("BSIT", 2, 2, BSITterm2_year2, courses_term2)
        add_courses_from_table("BSIT", 2, 3, BSITterm2_year3, courses_term2)
        add_courses_from_table("BSIT", 2, 4, BSITterm2_year4, courses_term2)

        add_courses_from_table("BSIT", 3, 1, BSITterm3_year1, courses_term3)
        add_courses_from_table("BSIT", 3, 2, BSITterm3_year2, courses_term3)
        add_courses_from_table("BSIT", 3, 3, BSITterm3_year3, courses_term3)
        add_courses_from_table("BSIT", 3, 4, BSITterm3_year4, courses_term3)

        # BSIS
        add_courses_from_table("BSIS", 1, 1, BSISterm1_year1, courses_term1)
        add_courses_from_table("BSIS", 1, 2, BSISterm1_year2, courses_term1)
        add_courses_from_table("BSIS", 1, 3, BSISterm1_year3, courses_term1)
        add_courses_from_table("BSIS", 1, 4, BSISterm1_year4, courses_term1)

        add_courses_from_table("BSIS", 2, 1, BSISterm2_year1, courses_term2)
        add_courses_from_table("BSIS", 2, 2, BSISterm2_year2, courses_term2)
        add_courses_from_table("BSIS", 2, 3, BSISterm2_year3, courses_term2)
        add_courses_from_table("BSIS", 2, 4, BSISterm2_year4, courses_term2)

        add_courses_from_table("BSIS", 3, 1, BSISterm3_year1, courses_term3)
        add_courses_from_table("BSIS", 3, 2, BSISterm3_year2, courses_term3)
        add_courses_from_table("BSIS", 3, 3, BSISterm3_year3, courses_term3)
        add_courses_from_table("BSIS", 3, 4, BSISterm3_year4, courses_term3)

        # BSCS
        add_courses_from_table("BSCS", 1, 1, BSCSterm1_year1, courses_term1)
        add_courses_from_table("BSCS", 1, 2, BSCSterm1_year2, courses_term1)
        add_courses_from_table("BSCS", 1, 3, BSCSterm1_year3, courses_term1)
        add_courses_from_table("BSCS", 1, 4, BSCSterm1_year4, courses_term1)

        add_courses_from_table("BSCS", 2, 1, BSCSterm2_year1, courses_term2)
        add_courses_from_table("BSCS", 2, 2, BSCSterm2_year2, courses_term2)
        add_courses_from_table("BSCS", 2, 3, BSCSterm2_year3, courses_term2)
        add_courses_from_table("BSCS", 2, 4, BSCSterm2_year4, courses_term2)

        add_courses_from_table("BSCS", 3, 1, BSCSterm3_year1, courses_term3)
        add_courses_from_table("BSCS", 3, 2, BSCSterm3_year2, courses_term3)
        add_courses_from_table("BSCS", 3, 3, BSCSterm3_year3, courses_term3)
        add_courses_from_table("BSCS", 3, 4, BSCSterm3_year4, courses_term3)

    add_all_terms()

    # ------------------ BUILD COURSE TITLE MAP ------------------
    def build_course_title_map():
        """Scan the hardcoded course tables and return a mapping code -> title."""
        tables = [
            BSITterm1_year1, BSITterm1_year2, BSITterm1_year3, BSITterm1_year4,
            BSITterm2_year1, BSITterm2_year2, BSITterm2_year3, BSITterm2_year4,
            BSITterm3_year1, BSITterm3_year2, BSITterm3_year3, BSITterm3_year4,
            BSISterm1_year1, BSISterm1_year2, BSISterm1_year3, BSISterm1_year4,
            BSISterm2_year1, BSISterm2_year2, BSISterm2_year3, BSISterm2_year4,
            BSISterm3_year1, BSISterm3_year2, BSISterm3_year3, BSISterm3_year4,
            BSCSterm1_year1, BSCSterm1_year2, BSCSterm1_year3, BSCSterm1_year4,
            BSCSterm2_year1, BSCSterm2_year2, BSCSterm2_year3, BSCSterm2_year4,
            BSCSterm3_year1, BSCSterm3_year2, BSCSterm3_year3, BSCSterm3_year4,
        ]
        m = {}
        for t in tables:
            for row in t:
                if not isinstance(row, (list, tuple)) or len(row) < 2:
                    continue
                code = str(row[0]).strip()
                title = str(row[1]).strip() if len(row) > 1 else ""
                if code:
                    m.setdefault(code, title)
        return m

    course_title_map = build_course_title_map()

    print(f"\nLoaded term counts: T1={len(courses_term1)} T2={len(courses_term2)} T3={len(courses_term3)}")

    # ------------------ SCHEDULER CONFIG (rooms, days, times) ------------------
    DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    # Split week: first 3 days = face-to-face, last 3 days = virtual
    FTF_DAYS = DAYS[:3]
    VIRTUAL_DAYS = DAYS[3:]
    START_MIN = 7 * 60    # 7:00 AM
    END_MIN = 21 * 60     # 9:00 PM
    LUNCH_START = 12 * 60
    LUNCH_END = 13 * 60
    LECTURE_ROOMS = ["203", "204"]
    LAB_ROOMS = ["COMLAB1", "COMLAB5", "COMLAB6"]

    def minutes_to_time(total):
        """Convert minutes-from-midnight to readable time like '7:00AM'."""
        hour = total // 60
        minute = total % 60
        suffix = "AM" if hour < 12 else "PM"
        show_hour = hour % 12 or 12
        return f"{show_hour}:{minute:02d}{suffix}"

    def _merge_intervals(intervals):
        """Merge and sort intervals list of (s,e)."""
        if not intervals:
            return []
        iv = sorted(intervals)
        merged = [iv[0]]
        for s, e in iv[1:]:
            last_s, last_e = merged[-1]
            if s <= last_e:
                merged[-1] = (last_s, max(last_e, e))
            else:
                merged.append((s, e))
        return merged

    def find_earliest_slot(room_busy, section_busy, duration, allowed_days=None, section_modality_map=None, desired_modality=None):
        """
        Find earliest (day, start) where both room_busy[day] and section_busy[day]
        allow a contiguous slot of `duration` minutes between START_MIN and END_MIN.
        Lunch interval (LUNCH_START,LUNCH_END) is treated as busy.
        room_busy and section_busy are dict day->list of (s,e).
        allowed_days: optional list of days to restrict search.
        section_modality_map: dict day->'FTF'|'VIRTUAL'|None to prevent mixing modalities.
        desired_modality: if provided, only days with None or matching modality are allowed.
        Returns (day, start_min) or None.
        """
        days_to_check = allowed_days if allowed_days is not None else DAYS
        candidates = []
        for day in days_to_check:
            # if modality constraint prevents using this day, skip
            if section_modality_map is not None and desired_modality is not None:
                m = section_modality_map.get(day)
                if m is not None and m != desired_modality:
                    continue

            # combine busy intervals for this day (include lunch as busy)
            busy = []
            busy.extend(room_busy.get(day, []))
            busy.extend(section_busy.get(day, []))
            busy.append((LUNCH_START, LUNCH_END))
            busy = _merge_intervals(busy)

            # before first busy interval
            if busy:
                first_start = busy[0][0]
                if first_start - START_MIN >= duration and START_MIN + duration <= END_MIN:
                    candidates.append((START_MIN, day))
            else:
                if START_MIN + duration <= END_MIN and not (START_MIN < LUNCH_END and START_MIN + duration > LUNCH_START):
                    candidates.append((START_MIN, day))

            # between merged intervals
            for i in range(len(busy) - 1):
                end_now = busy[i][1]
                start_next = busy[i+1][0]
                if start_next - end_now >= duration and end_now + duration <= END_MIN:
                    candidates.append((end_now, day))

            # after last
            last_end = busy[-1][1]
            if last_end + duration <= END_MIN:
                candidates.append((last_end, day))

        if not candidates:
            return None
        # pick candidate with minimal start_min, tie-break by day order
        candidates.sort(key=lambda x: (x[0], DAYS.index(x[1])))
        start_min, day = candidates[0]
        return day, start_min

    def build_session_blocks_for_course(course):
        """
        Given course dict with lec_minutes and lab_minutes, return list of blocks:
        [{'component':'LEC'|'LAB', 'duration': <minutes>, 'virtual': bool}]
        For year 1 and year 2 courses the second session of each component is marked virtual.
        """
        blocks = []
        lec_minutes = int(course.get("lec_minutes", 0))
        lab_minutes = int(course.get("lab_minutes", 0))
        # treat years 1 and 2 as hybrid: second session of each component is virtual
        is_hybrid_year = int(course.get("year", 0)) in (1, 2)

        # If both zero, fallback to a default two lecture sessions
        if lec_minutes == 0 and lab_minutes == 0:
            total = 160
            half = total // 2
            # first session on-site, second session virtual for year 1/2
            blocks.append({"component": "LEC", "duration": half, "virtual": False})
            blocks.append({"component": "LEC", "duration": total - half, "virtual": bool(is_hybrid_year)})
            return blocks

        # lecture component
        # Only split into two sessions if total lecture time > 2 hours (120 minutes).
        if lec_minutes > 0:
            if lec_minutes > 120:
                half = lec_minutes // 2
                if half < 60:
                    half = 60
                blocks.append({"component": "LEC", "duration": half, "virtual": False})
                blocks.append({"component": "LEC", "duration": max(lec_minutes - half, 60), "virtual": bool(is_hybrid_year)})
            else:
                # single on-site lecture session when total <= 2 hours
                blocks.append({"component": "LEC", "duration": lec_minutes, "virtual": False})

        # lab component: 2 sessions
        # Only split lab into two sessions if total lab time > 2 hours (120 minutes).
        if lab_minutes > 0:
            if lab_minutes > 120:
                half = lab_minutes // 2
                if half < 60:
                    half = 60
                blocks.append({"component": "LAB", "duration": half, "virtual": False})
                blocks.append({"component": "LAB", "duration": max(lab_minutes - half, 60), "virtual": bool(is_hybrid_year)})
            else:
                # single on-site lab session when total <= 2 hours
                blocks.append({"component": "LAB", "duration": lab_minutes, "virtual": False})

        return blocks

    def schedule_all_courses_global(courses, sections_map, term=1):
        """
        Schedule all courses (filtered by term). Virtual blocks are recorded
        but do not occupy rooms. Virtual blocks are assigned a day/start/end
        that does not overlap with other sessions for the same section.

        This version alternates the 3-days-FTF / 3-days-VIRTUAL split per
        section within the same program+year: sections at even indices use
        FTF_DAYS as FTF and VIRTUAL_DAYS as virtual; odd indices are flipped.
        """
        room_schedule = {r: {d: [] for d in DAYS} for r in (LECTURE_ROOMS + LAB_ROOMS)}
        section_schedule = {}
        section_modality = {}  # section -> day->'FTF'|'VIRTUAL'|None

        # Prepare alternating split per section (per program+year)
        section_day_split = {}  # sec -> {'FTF': [...], 'VIRTUAL': [...]}
        for prog in sections_map:
            for y, secs in sections_map[prog].items():
                for idx, sec in enumerate(secs):
                    # even index => pattern A, odd index => flipped pattern
                    if idx % 2 == 0:
                        section_day_split[sec] = {"FTF": FTF_DAYS, "VIRTUAL": VIRTUAL_DAYS}
                    else:
                        section_day_split[sec] = {"FTF": VIRTUAL_DAYS, "VIRTUAL": FTF_DAYS}

        for prog in sections_map:
            for y, secs in sections_map[prog].items():
                for sec in secs:
                    section_schedule[sec] = {d: [] for d in DAYS}
                    section_modality[sec] = {d: None for d in DAYS}
                    # ensure split exists for any section (fallback to default)
                    section_day_split.setdefault(sec, {"FTF": FTF_DAYS, "VIRTUAL": VIRTUAL_DAYS})

        courses_filtered = [c for c in courses if c.get("term") == term]
        courses_sorted = sorted(
            courses_filtered,
            key=lambda c: (
                c.get("year", 999),
                -(c.get("lec_minutes", 0) + c.get("lab_minutes", 0)),
                c.get("program", ""),
                c.get("code", "")
            )
        )

        scheduled = []

        for course in courses_sorted:
            blocks = build_session_blocks_for_course(course)
            prog = course.get("program")
            year = course.get("year")
            secs = sections_map.get(prog, {}).get(year, [])
            for sec in secs:
                sec_busy = section_schedule[sec]
                sec_mod_map = section_modality[sec]
                sec_split = section_day_split.get(sec, {"FTF": FTF_DAYS, "VIRTUAL": VIRTUAL_DAYS})
                for blk in blocks:
                    comp = blk["component"]
                    dur = blk["duration"]
                    is_virtual = bool(blk.get("virtual"))

                    # Years 1 and 2 use the alternating 3-days-FTF / 3-days-VIRTUAL split
                    if int(year) in (1, 2):
                        allowed_for_block = sec_split["VIRTUAL"] if is_virtual else sec_split["FTF"]
                        desired_modality = "VIRTUAL" if is_virtual else "FTF"
                    else:
                        allowed_for_block = None
                        desired_modality = "FTF"  # non-first/second-year are FTF by default

                    if is_virtual:
                        # no room constraints for virtual, but respect modality/day split
                        tmp_room_busy = {d: [] for d in DAYS}
                        day_start = find_earliest_slot(tmp_room_busy, sec_busy, dur,
                                                      allowed_days=allowed_for_block,
                                                      section_modality_map=sec_mod_map,
                                                      desired_modality=desired_modality)
                        if day_start is None:
                            # fallback: record virtual without times (should be rare)
                            scheduled.append({
                                "course_code": course["code"],
                                "section": sec,
                                "term": term,
                                "year": year,
                                "day": "VIRTUAL",
                                "start_time": "",
                                "end_time": "",
                                "room": "VIRTUAL",
                                "component": comp,
                                "duration_min": dur,
                                "virtual": True,
                            })
                            continue
                        day, start_min = day_start
                        end_min = start_min + dur
                        # reserve section time and set modality so no mixing on that day
                        section_schedule[sec][day].append((start_min, end_min))
                        section_modality[sec][day] = "VIRTUAL"
                        scheduled.append({
                            "course_code": course["code"],
                            "section": sec,
                            "term": term,
                            "year": year,
                            "day": day,
                            "start_time": minutes_to_time(start_min),
                            "end_time": minutes_to_time(end_min),
                            "room": "VIRTUAL",
                            "component": comp,
                            "duration_min": dur,
                            "virtual": True,
                        })
                        continue

                    # On-site (FTF) scheduling: respect modality/day split and avoid days already marked VIRTUAL
                    rooms = LECTURE_ROOMS if comp == "LEC" else LAB_ROOMS
                    placed = False
                    best_choice = None
                    for room in rooms:
                        day_start = find_earliest_slot(room_schedule[room], sec_busy, dur,
                                                      allowed_days=allowed_for_block,
                                                      section_modality_map=sec_mod_map,
                                                      desired_modality=desired_modality)
                        if day_start is None:
                            continue
                        day, start_min = day_start
                        day_idx = DAYS.index(day)
                        candidate = (day_idx, start_min, room)
                        if best_choice is None or candidate < best_choice:
                            best_choice = candidate

                    if best_choice is not None:
                        day_idx, start_min, room = best_choice
                        day = DAYS[day_idx]
                        end_min = start_min + dur
                        room_schedule[room][day].append((start_min, end_min))
                        section_schedule[sec][day].append((start_min, end_min))
                        # mark day modality as FTF (prevents virtual on same day)
                        section_modality[sec][day] = "FTF"
                        scheduled.append({
                            "course_code": course["code"],
                            "section": sec,
                            "term": term,
                            "year": year,
                            "day": day,
                            "start_time": minutes_to_time(start_min),
                            "end_time": minutes_to_time(end_min),
                            "room": room,
                            "component": comp,
                            "duration_min": dur,
                            "virtual": False,
                        })
                        placed = True
                    if not placed:
                        print(f"[WARN] Could not place {course['code']} ({comp} {dur}min) for section {sec}")

        return scheduled

    # ------------------ INTEGRATE SCHEDULER CALL (BSIT year1 term1) ------------------
    # Place this call after your existing course-loading code in main()
    # Example: after 'courses' is built for BSIT year1 term1 you can call:

    # Run a global scheduler per term (terms are isolated)
    scheduled_all_t1 = schedule_all_courses_global(courses_term1, sections_map, term=1)
    scheduled_all_t2 = schedule_all_courses_global(courses_term2, sections_map, term=2)
    scheduled_all_t3 = schedule_all_courses_global(courses_term3, sections_map, term=3)
    # Group scheduled entries by section (built inside print_grouped)
    # Print results per term
    def print_grouped(scheduled_list, term_label):
        by_section = {}
        for s in scheduled_list:
            by_section.setdefault(s['section'], []).append(s)

        print(f"\nGenerated schedule for {term_label} (grouped by section) — using all rooms:")
        if not by_section:
            print("  (no scheduled entries)")
            return
        for sec in sorted(by_section.keys()):
            print(f"\n Section {sec}:")
            entries = by_section[sec]
            # sort: on-site sessions first by day/start, virtual last
            def sort_key(e):
                if e.get('virtual'):
                    return (1, 99, "")
                day = e.get('day', '')
                day_idx = DAYS.index(day) if day in DAYS else 0
                return (0, day_idx, e.get('start_time',''))
            for entry in sorted(entries, key=sort_key):
                vflag = "VIRTUAL" if entry.get('virtual') else "FTF"
                if entry.get('start_time') and entry.get('end_time'):
                    times = f"{entry['start_time']}-{entry['end_time']}"
                else:
                    times = ""
                room = entry.get('room', '')
                print(f"  {entry.get('day',''):3} {times:13} {entry['course_code']:10} {entry['component']:3} room:{room}  {vflag}")

    print_grouped(scheduled_all_t1, "TERM 1")
    print_grouped(scheduled_all_t2, "TERM 2")
    print_grouped(scheduled_all_t3, "TERM 3")

    # ------------------ CSV EXPORT ------------------
    def write_csv_for_term(scheduled_list, filename):
        # Columns: Section, Day(Mon-Sat)/VIRTUAL, StartTime, EndTime, CourseCode, CourseTitle, Lec/Lab, Room, Modality
        rows = []
        for s in scheduled_list:
            start_time = s.get('start_time','') or ''
            end_time = s.get('end_time','') or ''
            room = s.get('room','')
            code = s.get('course_code','')
            title = course_title_map.get(code, '')
            rows.append([
                s.get('section',''),
                s.get('day',''),
                start_time,
                end_time,
                code,
                title,
                s.get('component',''),
                room,
                "VIRTUAL" if s.get('virtual') else "FTF"
            ])
        # sort by section, day order (Mon..Sat), then start time
        rows.sort(key=lambda r: (r[0],
                                 DAYS.index(r[1]) if r[1] in DAYS else 6,
                                 r[2] or ''))
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Section','Day','StartTime','EndTime','CourseCode','CourseTitle','Lec/Lab','Room','Modality'])
                writer.writerows(rows)
            print(f"Wrote CSV: {filename}")
        except Exception as e:
            print(f"[ERROR] Could not write CSV {filename}: {e}")

    def export_csv_prompt():
        """Ask user (y/n) whether to export CSVs. Returns True if exported."""
        # If flag provided, export without asking
        if args.export_csv:
            write_csv_for_term(scheduled_all_t1, 'term1_schedule.csv')
            write_csv_for_term(scheduled_all_t2, 'term2_schedule.csv')
            write_csv_for_term(scheduled_all_t3, 'term3_schedule.csv')
            return True

        # interactive prompt
        try:
            resp = input('\nWould you like to export the schedules to CSV files? (y/n): ').strip().lower()
        except EOFError:
            resp = 'n'
        if resp in ('y', 'yes'):
            write_csv_for_term(scheduled_all_t1, 'term1_schedule.csv')
            write_csv_for_term(scheduled_all_t2, 'term2_schedule.csv')
            write_csv_for_term(scheduled_all_t3, 'term3_schedule.csv')
            return True
        print('CSV export skipped.')
        return False

    # call the prompt at end
    export_csv_prompt()

if __name__ == "__main__":
    main()