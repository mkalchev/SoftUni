#number of pages per book
num_pages_per_book = int(input())
#number of pages read per hour
num_pages_read_per_hour = int(input())
#number of days allowed to read each book
days_allowed_per_book = int(input())

#Общо време за четене на книгата
hours_req_per_book = num_pages_per_book / num_pages_read_per_hour
#Необходимите часове на ден
hours_per_day_per_book = hours_req_per_book // days_allowed_per_book


print(f"{hours_per_day_per_book} hours per day")
