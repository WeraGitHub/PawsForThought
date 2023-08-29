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