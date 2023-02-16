def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    student_count = 0
    for start, out in permanence_period:
        if not isinstance(start, int) or not isinstance(out, int):
            return None
        if start <= target_time <= out:
            student_count += 1
    return student_count