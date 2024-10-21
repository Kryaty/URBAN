number_of_finished_homeworks = 12
total_hours_spent= 1.5
name_of_course = "Python"
one_hour = 60
total_spent_in_minutes = total_hours_spent*one_hour
time_on_one_homework = (total_spent_in_minutes/number_of_finished_homeworks)
t = ","
print ("Курс:",name_of_course+t, "задач всего:", str (number_of_finished_homeworks)+t, "затрачено часов:", str (total_hours_spent)+t, "среднее время выполнения:", time_on_one_homework, "минут")
