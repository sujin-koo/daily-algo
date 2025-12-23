### naive version

def solution(id_list, report, k):
    # user -> list of users they reported (duplicates must be checked manually)
    reported_by_user = {}
    # user -> number of times they have been reported
    report_count = {}
    # user -> number of notification mails received
    mail_count = {}

    # Initialize data structures
    for user_id in id_list:
        reported_by_user[user_id] = []
        report_count[user_id] = 0
        mail_count[user_id] = 0

    # Collect reported users for each reporter
    # Duplicate reports (same reporter -> same reported user) are filtered manually
    for record in report:
        reporter, reported = record.split()
        if reported not in reported_by_user[reporter]:
            reported_by_user[reporter].append(reported)

    # Count how many times each user was reported
    # Users reported at least k times will be banned
    banned_users = {}
    for reporter in reported_by_user:
        for reported in reported_by_user[reporter]:
            report_count[reported] += 1
            if report_count[reported] >= k:
                banned_users[reported] = True

    # Count notification mails for each user
    answer = []
    for reporter in reported_by_user:
        for reported in reported_by_user[reporter]:
            if reported in banned_users:
                mail_count[reporter] += 1
        answer.append(mail_count[reporter])

    return answer



### refined version1
def solution(id_list, report, k):
    # user -> set of users they reported (duplicates automatically removed)
    reported_by_user = {user_id: set() for user_id in id_list}
    # user -> number of times they have been reported
    report_count = {user_id: 0 for user_id in id_list}
    # user -> number of notification mails received
    mail_count = {user_id: 0 for user_id in id_list}

    # Build report relationships (duplicate reports removed via set)
    for record in report:
        reporter, reported = record.split()
        reported_by_user[reporter].add(reported)

    # Count how many times each user was reported
    for reporter in reported_by_user:
        for reported in reported_by_user[reporter]:
            report_count[reported] += 1

    # Identify banned users (reported at least k times)
    banned_users = {user for user, cnt in report_count.items() if cnt >= k}

    # Count notification mails for each user (preserving id_list order)
    answer = []
    for user_id in id_list:
        count = 0
        for reported in reported_by_user[user_id]:
            if reported in banned_users:
                count += 1
        answer.append(count)

    return answer




### refined version2
from collections import Counter

def solution(id_list, report, k):
    # Step 1: Remove duplicate reports (same reporter -> same reported user)
    unique_reports = set(report)

    # Step 2: Count how many times each user was reported
    reported_users = [record.split()[1] for record in unique_reports]
    report_count = Counter(reported_users)

    # Step 3: Identify banned users (reported at least k times)
    banned_users = {user for user, cnt in report_count.items() if cnt >= k}

    # Step 4: Count notification mails for each user
    mail_count = {user: 0 for user in id_list}
    for record in unique_reports:
        reporter, reported = record.split()
        if reported in banned_users:
            mail_count[reporter] += 1

    # Return results in the order of id_list
    return [mail_count[user] for user in id_list]
