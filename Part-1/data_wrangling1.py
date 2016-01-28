import unicodecsv
from datetime import datetime

enrollments_filepath = '../Dataset/enrollments.csv'
submissions_filepath = '../Dataset/project_submissions.csv'
engagement_filepath = '../Dataset/daily_engagement.csv'

def csv2list(filename):
	with open(filename,'rb') as f:
		iterator = unicodecsv.DictReader(f)
		return list(iterator)

def parse_date(date_s):
	if date_s == '':
		return None
	else:
		return datetime.strptime(date_s , '%Y-%m-%d')
def parse_int(i):
	if i == '':
		return None
	else:
		return int(i)

def parse_double(double):
	if double == '':
		return None
	else:
		return float(double)
def parse_boolean(strg):
	if strg == 'True':
		return True
	else:
		return False


enrollments = csv2list(enrollments_filepath)
engagements = csv2list(engagement_filepath)
submissions = csv2list(submissions_filepath)

# Format Enrollment data
for enrollment in enrollments:
	enrollment['is_udacity'] = parse_boolean(enrollment['is_udacity'])
	enrollment['is_canceled'] = parse_boolean(enrollment['is_canceled'])
	enrollment['join_date'] = parse_date(enrollment['join_date'])
	enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
	enrollment['days_to_cancel'] = parse_int(enrollment['days_to_cancel'])

# Format Submission Data
for engagement in engagements:
	engagement['lessons_completed'] = parse_int(parse_double(engagement['lessons_completed']))
	engagement['num_courses_visited'] = parse_int(parse_double(engagement['num_courses_visited']))
	engagement['projects_completed'] = parse_int(parse_double(engagement['projects_completed']))
	engagement['utc_date'] = parse_date(engagement['utc_date'])
# Format engagements Data
for submission in submissions:
	submission['completion_date'] = parse_date(submission['completion_date'])
	submission['creation_date'] = parse_date(submission['creation_date'])

# print enrollments[0]
# print engagements[0]
#print submissions[0]

enrollment_num_rows = len(enrollments)
engagement_num_rows = len(engagements)
submission_num_rows = len(submissions)
enrollment_num_rows_unique = len(set(dic['account_key'] for dic in enrollments))
submissions_num_rows_unique = len(set(dic['account_key'] for dic in submissions))
engagement_num_rows_unique = len(set(dic['acct'] for dic in engagements))

print engagement_num_rows
print enrollment_num_rows
print submission_num_rows
print enrollment_num_rows_unique
print submissions_num_rows_unique
print engagement_num_rows_unique



