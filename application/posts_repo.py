from application.post import Post
from _datetime import datetime


posts = []

post1 = Post("Week 1 of Sky DevOps Bootcamp", datetime(2023, 8, 12),
             """First two days were dedicated to DevOps Foundation Course.
                <br />                
                We were taught about the culture, community, tools and practices by QA Tutor Dave Tomlinson. 
                It was useful but intense! Glad we have the presentation's slides for us to keep. 
                I had an opportunity to work in group with two of my new colleagues, which was nice. Both of them seemed 
                very kind and knowledgeable. I'm looking forward to spending more time with them in the future.
                My main take always are: DevOps is lots of different things: tools, practices, culture and movement; 
                I love the idea of creating safe environment where people can fail fast and develop quicker because of 
                it; agile practices make much more sense then the waterfall one; breaking silos; endless list of DevOps 
                tools (see the periodic table link) and small but often if not continuous changes. 
                <br />
                <br />
                Day 3 to day 5 we delved into the Architecting on AWS course. 
                <br />
                I enjoyed the labs and was glad we had someone to ask questions to - Richard Kelly. 
                Information packed three days, I'm glad I was familiar with AWS before we started this course. 
                To make sure I follow and understand each lesson and lab, I've spent some time on creating my own 
                graphs. I am certain this will help me memorise all the security layers and checkpoints and VPC 
                components. I now know and understand what a Load Balancer is! 
                Our teacher went all the way and beyond and even helped me resolve my own AWS conundrum (displaying the 
                cost widget on my AMI user account, despite having attached right policies to my userm I couldn't see 
                it. Richard pointed me to the additional setting that needs to be enabled for it to work). I am hoping 
                to take the AWS Certified Solutions Architect - Associate exam at some point in the future.
                <br />
                <br />
                Week one - done! 🥳
                
                """,
             {
                "The (Short) History of DevOps": "https://www.youtube.com/watch?v=o7-IuYS0iSE",
                "Start with 'Why' - TED Talk from Simon Sinek": "https://www.youtube.com/watch?v=2Ss78LfY3nE",
                "Gene Kim defines the 3 ways of the Pheonix Project": "https://www.youtube.com/watch?v=nUOXDEvplRc",
                "4 Professional Guides Continuous Integration Continuous Delivery": "https://www.youtube.com/watch?v=AL6vmbITfiQ",
                "DevOps Releasing": "https://www.youtube.com/watch?v=Q2zKeqFw7xg",
                "Spotify Engineering Culture (by Henrik Kniberg)": "https://www.youtube.com/watch?v=4GK1NDTWbkY",
                "Spotify Engineering Culture part 2": "https://www.youtube.com/watch?v=rzoyryY2STQ",
                "The DevOps Toolchain": "https://www.youtube.com/watch?v=bwE8aFPAzj8",
                "Keynote: Double the Awesome - Dr. Nicole Forsgren": "https://www.youtube.com/watch?v=c2VwRKAyQ-M",
                "DevOps: A Culture of Sharing": "https://www.youtube.com/watch?v=8aJHtjp--3U",
                "DevOps Tools Periodic Table by DigitalAi": "https://digital.ai/learn/devops-periodic-table/",
                "Interesting tool to write emails to future self": "https://www.futureme.org/",
                "AWS Well-Architected Framework": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
                "AWS Well-Architected Labs": "https://www.wellarchitectedlabs.com/",
                "AWS Global Infrastructure": "https://aws.amazon.com/about-aws/global-infrastructure/",
                "The Bits and Bytes of Computer Networking - course recommended by the tutor - Richard": "https://www.coursera.org/learn/computer-networking",
                "Instance Scheduler on AWS": "https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/",
                "AWS Solutions Library": "https://aws.amazon.com/solutions/ ",
                "AWS Permissions Boundaries 1": "https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/",
                "AWS Permissions Boundaries 2": "https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/",
                "S3 Storage 1": "https://aws.amazon.com/blogs/storage/electronic-arts-significantly-optimizes-storage-costs-and-operational-overhead-using-amazon-s3-and-s3-glacier/",
                "S3 Storage 2": "https://aws.amazon.com/blogs/storage/how-amagi-uses-amazon-s3-glacier-instant-retrieval-to-optimize-media-storage-costs/",
                "Exam 1": "https://aws.amazon.com/certification/certified-solutions-architect-associate/?ch=tile&tile=getstarted",
                "Exam 2": "https://explore.skillbuilder.aws/learn/course/14760/play/68384/introduction-to-aws-certified-solutions-architect-associate-saa-c03",
                "Exam 3": "https://explore.skillbuilder.aws/learn/course/internal/view/elearning/13266/aws-certified-solutions-architect-associate-official-practice-question-set-saa-c03-english"
             },
    "1DevOps2days.png", "1AWSday1.png", "1AWSday2.png", "1AWSday3.png", "1AWSgraph1.png", "1AWSgraph2.png",
             "1AWSgraph3.png", "1AWSgraph6.png", "1AWSgraph4.png", "1AWSgraph5.png")
posts.append(post1)

post2 = Post('Week 2 of Sky DevOps Bootcamp', datetime(2023, 8, 19),
             """During fun packed week 2, we were introduced to Python 3.
              <br />
              We covered simple concepts like variables and string handling, progressed to more complex topics such as 
              flow control and collections, and delved into a slightly more advanced area - exception handling. On 
              Friday we had cyber-security tournament! From the points point of view my team lost, but if you look at
              how much we learned I believe we are the real winners :) 
              <br />
              Since I was already familiar with Python, this week was relatively easy for me, except for Friday! 
              I definitely need to learn more about exception handling and security. 
              <br />
              Throughout the week, we were assigned numerous coding exercises to complete in pairs and groups of three. 
              This proved to be a fantastic way to learn, spend time in smaller groups, and get to know each other 
              better.
              <br />
              Another exciting development was the division of our cohort into two groups. Each morning, we quizzed each 
              other on the previously learned material, competing for points. 
              I think now everyone has a good understanding of Python now and is ready to start working on 
              our showcase projects, hopefully starting from the middle of next week.
              <br />
              Week 2 - smashed! 😎
                """,
             {},
             "2debugging.png", "2exception1.png", "2function_annotations.png", "2function_documentation.png",
             "2inheritance.png", "2lambda.png", "2reading_files.png", "2regex.png", "2regex2.png", "2sets.png",
             "2sets2.png", "2stderr.png")
posts.append(post2)

post3 = Post('Week 3 of Sky DevOps Bootcamp', datetime(2023, 8, 25),
             """
              This week's main themes were cyber-security, Flask and Agile Fundamentals.
              <br />
              I really enjoyed the 2 days "Secure by Design" with Ali, it was all completely new for me. We were given 
              access to a sandbox environment to practice our hacking and hacking-related defensive skills. It is a bit 
              slow but safe.We were cautioned not to engage in ethical hacking without necessary permission, as this 
              would be illegal and could lead to trouble. The importance of changing  your wifi router's default 
              password, least privilege rule and to never ever ever trust data.
              <br >              
              I have finished coding this blog and deployed it this week. I'm happy with how pretty and pretty close it 
              is to my original design (in Figma).
              <br />
              Finally, our cohort was taught the basics of Flask, and we were given a mini-project to work on while 
              learning how to practice Agile ways of working. I'm really pleased with what my teammates and I have 
              achieved! Below is a snippet of the Little Sky Feedback page; we even made it live by hosting an Apache 
              server on an EC2 instance on AWS. We focused on the basic requirements first, rather than packing it with 
              features and running out of time :) Individuals and interactions over processes and tools with working 
              software over comprehensive documentation.
              <br />
              Week 3 - conquered! 👑
                """,
             {"DVWA - Damn Vulnerable Web Application": "https://github.com/digininja/DVWA",
              "Google Hacking Database (GHDB)": "https://www.exploit-db.com/google-hacking-database",
              "The Cyber Kill Chain": "https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html",
              "Throwback Attack: Chinese hackers steal plans for the F-35 fighter in a supply chain heist": "https://www.industrialcybersecuritypulse.com/networks/throwback-attack-chinese-hackers-steal-plans-for-the-f-35-fighter-in-a-supply-chain-heist/",
              "OWASP Top 10": "https://owasp.org/www-project-top-ten/",
              "Hash calculator": "https://www.fileformat.info/tool/hash.htm",
              "Colonial Pipeline ransomware attack": "https://en.wikipedia.org/wiki/Colonial_Pipeline_ransomware_attack",
              "Scrum Guides": "https://scrumguides.org/"
              },
             "3figma.png", "3ACL.png", "3SD3.png", "3stride.png", "3injection.png", "3securedesign.png",
             "3notrust.png", "3test.png", "3value.png", "3jinja.png", "3stakeholders.png", "3invest.png", "3boehm.png",
             "3bob.png"
             )
posts.append(post3)


post4 = Post('Week 4 of Sky DevOps Bootcamp', datetime(2023, 9, 2),
             """
              This week's focus was on Jenkins and Docker 😌
              <br />
              I feel like we're finally getting into the juicy stuff - DevOps tools!
              <br />
              <br />
              We also had a Python workshop hosted by a few people from Sky, where we were tasked to build an API 
              endpoint for a book library application! Lots of useful information, some of which I hope to use in our 
              upcoming showcase project.
              <br />
              The week ended with a Google Here workshop! We met a person who works at Google and had some fun with 
              online GCP-related games.
              <br />
              A flare up of my health conditions started this week, hope it will settle by the end of the weekend..🤞
              <br />
              Week 4 - BOOM 🤩
                """,
             {"Google Cloud Skills Boost": "https://www.cloudskillsboost.google/",
              "A Tour of Go": "https://go.dev/tour/welcome/1"
              },
             "4ghero.png"
             )
posts.append(post4)


post5 = Post('Week 5, Final week of Sky DevOps Bootcamp', datetime(2023, 9, 10),
             """
              We had 3 workshops: CI/CD, monitoring and security! We also started learning Terraform and had some time 
              to work on our projects and presentations for Friday.
              <br />
              On Friday, we were presenting our bootcamp projects, and I think we did great, in fact, both teams did 
              great! We learned lots and had some fun along the way :)
              <br />
              That was also our last week with Victoria, our main bootcamp teacher. She is a fantastic, knowledgeable 
              and great at what she does, we were lucky to have her.
              <br />              
              <br />
              Highlight of the week: tinkering with Terraform
              <br />
              Highlight of the bootcamp: getting to know my new colleagues
              <br />
              <br />
              Week 5 - all right!
              <br />
              I'm looking forward to seeing what next week will bring us.                """,
             {"Agile Ninjas repo": "https://github.com/WeraGitHub/AgileNinjasProject"
              },
             "5monitoring.png", "5security.png", "5terraform.png", "5slide.png", "5agenda.png", "5repo.png"
             )
posts.append(post5)


post6 = Post('My first ever Hackathon', datetime(2023, 9, 16),
             """
              This week was a fun induction week. We officially met our manager, previous year's grads, had some fun ice
               breakers and a HACKATHON!
              <br />
              OK, being all new to the team and the codebase and knowing nothing about Go Lang, I didn't contribute much 
              to our project. But it didn't stop me from being part of the team and enjoying meeting new people, 
              shadowing them, and trying to read the Go files. It was great to be thrown into deep waters, but in a safe
               environment. Deep waters but in life jacket or with floating sleeves??
              <br />
              <br />
              This week was also the first week for my colleagues to be in the office while I stayed at home. My manager
               and my colleagues made me feel included and made sure I was able to take part in everything that was 
               planned for this week. That was tremendously important to me and something I was worried about 
               beforehand. I felt welcomed despite my physical abilities, and it feels truly heartwarming.
              <br />
              Still, it's even more important to make light of the situation, so I am attaching a picture puzzle for 
              Power Rangers fans, asking you to find 3 differences 🫣 
              <br />
              <br />
              Next week will be interesting... 👀👀👀👀👀
              """,
             {},
             "6wera1.png", "6zordon.png"
             )
posts.append(post6)


post7 = Post('Google Week', datetime(2023, 9, 22),
             """
             Say whaaat, we were invited to Google office!
             <br />
             <br />
              On Monday I ventured out to Kings Cross, London. My team and me had some free lunch, and as we were 
              finishing, we were asked to evacuate... Which gave me a chance to meet some lovely doggos, two of them 
              were sniffer dogs working at Google. I asked their handler for permission to say hello and they said yes 
              (: I wish my dog would get a job 🐾
              <br />
              After a thankfully non-eventful evacuation, we were let back in and had great day. We talked about gcp,
              sustainability, met a few people, enjoyed some more (free) lovely food and snacks and even had a few 
              laughs. Later, I had a chance to go for a drink and a chat with my colleagues.
              <br />
              <br />
              I took Tuesday off to rest, and for the rest of the week I worked from home.
              <br />
              After learning lots about google cloud offerings and possible certifications, we did a mock exam on 
              Friday.
              <br />
              <br />
              Even a few years ago, if anyone had told me that I would be invited to Google, I would have strongly 
              disbelieved it. Ha! I still can't believe it!
              """,
             {},
             "7dog.png", "7dogs.png", "7view2.png", "7pass.png", "7inside.png", "7view.png"
             )
posts.append(post7)

post8 = Post('Project Research Week', datetime(2023, 9, 30),
             """
             This week, we were divided into pairs and given the task of researching a [CONFIDENTIAL] project. I had the
              pleasure of being paired with someone I had not worked closely with before, which was perfect. Planning 
              the work and dividing tasks between us and working with him was super easy! We are both good 
              communicators, and I feel like we gave each other space to play to our strengths. Overall, we smashed this
               week's objectives. I think we managed to get to know each other better and hopefully got one step closer 
               to becoming friends :) .
             <br />
             <br />
             I managed to get the Terraform file working! The file that I am talking about is for our infrastructure 
             setup for our bootcamp project. There is a load balancer, auto scaling group, RDS and our app image running
              on private EC2 🫡. We are talking proper bells and whistles here and I'm so happy it works, but I'm sure 
              there are plenty of things I could have done better since this is my first Terraform file. Well, 
              technically, it's my second. The first one was for creating a single resource on AWS.
             <br />
             <br />
             I will try to make my mission to get some silly pictures for next week. 
             For now, enjoy my home office manager sleeping on the job 🙄
             """,
             {},
             "8dog.png"
             )
posts.append(post8)

#
# Example qustions:
#
# Experiences gone and still to come:
#
# What you have learned (or are struggling to learn):
#
# Specific characteristics you have shown or need to develop:
#
# How it relates to what you already know:
#
# How it relates to your more specific goals:
#
# How it relates to your strengths and weaknesses:
#
# How do you feel about each of your reflections? Do you think you are: Growing your understanding of yourself? Changing your thoughts and mindset?
#
# Changing in your perception of who you are?