import os

def docker_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: Configure Docker
	     \t\t Press 2: Start Docker services
             \t\t Press 3: List OS images
	     \t\t Press 4: Pull OS Images
             \t\t Press 5: List running containers
             \t\t Press 6: Launch a container
             \t\t Press 7: Start a container
             \t\t Press 8: Stop a container
             \t\t Press 10: Delete a container
	     \t\t Press 11: Configure httpd server inside a container
             \t\t Press 9: Back
             \t\t Press 0: Exit""")
    print("\n\t\t####################################################################")



def docker_functions(loc, choice, ip=""):
    if loc=="local":
        if choice==1:
            os.system("tput setaf 4")
            if os.system("rpm -q docker-ce")==0:
                os.system("tput setaf 3")
                print("Docker is already installed")
            else:
                os.system("tput setaf 1")
                print("Docker is not installed")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==2:
            os.system("tput setaf 4")
            print("Starting Docker services.......")
            os.system("tput setaf 7")
            if os.system("systemctl start docker")==0:
                os.system("tput setaf 3")
                print("Service started successfully")
            else:
                os.system("tput setaf 1")
                print("Failed to start the service")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==3:
            os.system("tput setaf 4")
            print("Retrieving available OS images.......")
            os.system("tput setaf 7")
            if os.system("docker images")!=0:
                os.system("tput setaf 1")
                print("Failed")
            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        
        elif choice==4:
            os.system("tput setaf 4")
            print("Enter the name of the image to be pulled : ")
            os.system("tput setaf 7")
            image = input()
            os.system("tput setaf 3")
            print("Pulling image.........")
            os.system("tput setaf 7")
            if os.system("docker pull %s" %image)==0:
                os.system("tput setaf 3")
                print("Image pulled successfully")
            else:
                os.system("tput setaf 1")
                print("Cannot pull the image")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        
        elif choice==5:
            os.system("tput setaf 4")
            print("Retrieving list of running containers.......")
            os.system("tput setaf 7")
            if os.system("docker ps")!=0:
                os.system("tput setaf 1")
                print("Failed")
            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        
        elif choice==6:
            os.system("tput setaf 4")
            print("Enter the name of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 4")
            print("Enter the name of the image: ")
            os.system("tput setaf 7")
            image = input()
            os.system("tput setaf 3")
            print("Launching container.........")
            os.system("tput setaf 7")
            if os.system("docker run -it --name %s %s" %(container, image))==0:
                os.system("tput setaf 3")
                print("Container launched successfully")
            else:
                os.system("tput setaf 1")
                print("Cannot launch the container")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==7:
            os.system("tput setaf 7")
            os.system("tput setaf 4")
            print("Enter the name/id of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 3")
            print("Starting container.....")
            os.system("tput setaf 7")
            if os.system("docker start %s" %container)==0:
                os.system("tput setaf 3")
                print("Container started")
            else:
                os.system("tput setaf 1")
                print("Cannot start the container")
            
        elif choice==8:
                os.system("tput setaf 4")
                print("Enter the name/id of the container : ")
                os.system("tput setaf 7")
                container = input()
                os.system("tput setaf 3")
                print("Stopping container.....")
                os.system("tput setaf 7")
                if os.system("docker stop %s" %container)==0:
                    os.system("tput setaf 3")
                    print("Container stopped")
                else:
                    os.system("tput setaf 1")
                    print("Cannot stop the container")

        elif choice==10:
            os.system("tput setaf 4")
            print("Enter the name/id of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 3")
            print("Deleting container.....")
            os.system("tput setaf 7")
            if os.system("docker rm -f %s" %container)==0:
                os.system("tput setaf 3")
                print("Container deleted")
            else:
                os.system("tput setaf 1")
                print("Cannot delete the container")

        elif choice==11:
            os.system("tput setaf 4")
            print("Enter the name/id of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 3")
            print("Configuring HTTPD Server.......")
            os.system("tput setaf 7")
            if os.system("docker exec %s yum install httpd -y" %container)==0:
                if os.system("docker exec %s /usr/sbin/httpd -k start" %container)==0:
                    os.system("tput setaf 3")
                    print("Apache Server configured successfully")
                else:
                    os.system("tput setaf 1")
                    print("Cannot start the services")
            else:
                os.system("tput setaf 1")
                print("Cannot install httpd")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        else:
            os.system("tput setaf 1")
            print("No such option")
            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")



    elif loc=="remote":
        if choice==1:
            os.system("tput setaf 4")
            if os.system("ssh %s rpm -q docker-ce" %ip)==0:
                os.system("tput setaf 3")
                print("Docker is already installed")
            else:
                os.system("tput setaf 1")
                print("Docker is not installed")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==2:
            os.system("tput setaf 4")
            print("Starting Docker services.......")
            os.system("tput setaf 7")
            if os.system("ssh %s systemctl start docker" %ip)==0:
                os.system("tput setaf 3")
                print("Service started successfully")
            else:
                os.system("tput setaf 1")
                print("Failed to start the service")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")
        
        elif choice==3:
            os.system("tput setaf 4")
            print("Retrieving available OS images.......")
            os.system("tput setaf 7")
            if os.system("ssh %s docker images" %remoteip)!=0:
                os.system("tput setaf 1")
                print("Failed")
            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")



        elif choice==4:
            os.system("tput setaf 4")
            print("Enter the name of the image to be pulled : ")
            os.system("tput setaf 7")
            image = input()
            os.system("tput setaf 3")
            print("Pulling image.........")
            os.system("tput setaf 7")
            if os.system("ssh %s docker pull %s" %(ip,image))==0:
                os.system("tput setaf 3")
                print("Image pulled successfully")
            else:
                os.system("tput setaf 1")
                print("Cannot pull the image")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==5:
            os.system("tput setaf 4")
            print("Retrieving list of running containers.......")
            os.system("tput setaf 7")
            if os.system("ssh %s docker ps" %remoteip)!=0:
                os.system("tput setaf 1")
                print("Failed")
            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        
        elif choice==6:
            os.system("tput setaf 4")
            print("Enter the name of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 4")
            print("Enter the name of the image: ")
            os.system("tput setaf 7")
            image = input()
            os.system("tput setaf 3")
            print("Launching container.........")
            os.system("tput setaf 7")
            if os.system("ssh %s docker run -it --name %s %s" %(ip,container, image))==0:
                os.system("tput setaf 3")
                print("Container launched successfully")
            else:
                os.system("tput setaf 1")
                print("Cannot launch the container")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==7:
            os.system("tput setaf 7")
            os.system("tput setaf 4")
            print("Enter the name/id of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 3")
            print("Starting container.....")
            os.system("tput setaf 7")
            if os.system("ssh %s docker start %s" %(ip,container))==0:
                os.system("tput setaf 3")
                print("Container started")
            else:
                os.system("tput setaf 1")
                print("Cannot start the container")
            
        elif choice==8:
                os.system("tput setaf 4")
                print("Enter the name/id of the container : ")
                os.system("tput setaf 7")
                container = input()
                os.system("tput setaf 3")
                print("Stopping container.....")
                os.system("tput setaf 7")
                if os.system("ssh %s docker stop %s" %(ip,container))==0:
                    os.system("tput setaf 3")
                    print("Container stopped")
                else:
                    os.system("tput setaf 1")
                    print("Cannot stop the container")

        elif choice==10:
            os.system("tput setaf 4")
            print("Enter the name/id of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 3")
            print("Deleting container.....")
            os.system("tput setaf 7")
            if os.system("ssh %s docker rm -f %s" %(ip,container))==0:
                os.system("tput setaf 3")
                print("Container deleted")
            else:
                os.system("tput setaf 1")
                print("Cannot delete the container")

        elif choice==11:
            os.system("tput setaf 4")
            print("Enter the name/id of the container : ")
            os.system("tput setaf 7")
            container = input()
            os.system("tput setaf 3")
            print("Configuring HTTPD Server.......")
            os.system("tput setaf 7")
            if os.system("ssh %s docker exec %s yum install httpd -y" %(ip,container))==0:
                if os.system("ssh %s docker exec %s /usr/sbin/httpd -k start" %(ip,container))==0:
                    os.system("tput setaf 3")
                    print("Apache Server configured successfully")
                else:
                    os.system("tput setaf 1")
                    print("Cannot start the services")
            else:
                os.system("tput setaf 1")
                print("Cannot install httpd")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        else:
            os.system("tput setaf 1")
            print("No such option")
            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")


