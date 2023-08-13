from application.post import Post
import datetime


posts = []

post1 = Post("Week 1", datetime.datetime(2023, 8, 12),
             """First two day were dedicated to DevOps Foundation Course.
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
                Day 3 to day 5 we were for Architecting on AWS course. 
                <br />
                I enjoyed the labs and was glad we had someone to ask questions to - Richard Kelly. 
                Information packed, I'm glad I was familiar with AWS before we started this course. 
                To make sure I follow and understand each lesson and lab I've spent some time on creating my own graphs. 
                I am sure this will help me memorise all the security layers and checkpoints and VPC components. I know 
                what a Load Balancer is now! 
                Our teacher went all the way and beyond and even helped me fix my own AWS conundrum (displaying the cost 
                widget on my AMI user account, despite having attached right policies to my user I couldn't see it. 
                Richard pointed me to the additional setting that needs to be enabled for it to work). I am hoping to 
                take the AWS Certified Solutions Architect - Associate exam at some point in the future.
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
             "1AWSgraph3.png", "1AWSgraph4.png", "1AWSgraph5.png", "1AWSgraph6.png")
posts.append(post1)

