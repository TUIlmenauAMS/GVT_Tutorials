#According to: https://nbgrader.readthedocs.io/en/stable/user_guide/managing_assignment_files.html#setting-up-the-exchange
c = get_config()
c.CourseDirectory.course_id = "GVT_seminars_ws2022" # The course ID
c.Exchange.root = "Path to your shared folder" # The path to your shared folder, something like /home/username/nextcloud
c.CourseDirectory.student_id = "Your matrikel number" # Your matrikel number
