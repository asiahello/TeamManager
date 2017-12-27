from django.contrib.auth.models import User

# COACHES

User.objects.create_user("c1_t12_c1", "c1_t12_c1@tm.com", "zaq12wsx")
User.objects.create_user("c2_t23_c1", "c2_t12_c1@tm.com", "zaq12wsx")
User.objects.create_user("c3_t31_c1", "c3_t12_c1@tm.com", "zaq12wsx")

User.objects.create_user("c1_t12_c2", "c1_t12_c2@tm.com", "zaq12wsx")
User.objects.create_user("c2_t23_c2", "c2_t12_c2@tm.com", "zaq12wsx")
User.objects.create_user("c3_t31_c2", "c3_t12_c2@tm.com", "zaq12wsx")

# PLAYERS

User.objects.create_user("p1_t1_c1", "p1_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p2_t1_c1", "p2_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p3_t1_c1", "p3_t1_c1@tm.com", "zaq12wsx")

User.objects.create_user("p1_t2_c1", "p1_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p2_t2_c1", "p2_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p3_t2_c1", "p3_t1_c1@tm.com", "zaq12wsx")

User.objects.create_user("p1_t3_c1", "p1_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p2_t3_c1", "p2_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p3_t3_c1", "p3_t1_c1@tm.com", "zaq12wsx")


User.objects.create_user("p1_t1_c2", "p1_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p2_t1_c2", "p2_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p3_t1_c2", "p3_t1_c1@tm.com", "zaq12wsx")

User.objects.create_user("p1_t2_c2", "p1_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p2_t2_c2", "p2_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p3_t2_c2", "p3_t1_c1@tm.com", "zaq12wsx")

User.objects.create_user("p1_t3_c2", "p1_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p2_t3_c2", "p2_t1_c1@tm.com", "zaq12wsx")
User.objects.create_user("p3_t3_c2", "p3_t1_c1@tm.com", "zaq12wsx")
