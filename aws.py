import os
import subprocess
#AWS main
def aws_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: Configure AWS CLI
             \t\t Press 2: Login to AWS account
             \t\t Press 3: AWS EC2
             \t\t Press 4: AWS EBS
             \t\t Press 5: AWS S3
             \t\t Press 6: AWS Cloudfront
             \t\t Press 7: IAM
             \t\t Press 9: Back
             \t\t Press 0: Exit""")
    print("\t\t####################################################################")


def aws_functions(loc, choice, ip=""):
    if loc=="local":
        if choice==1:
            os.system("tput setaf 4")
            print("Validating......")
            os.system("tput setaf 7")
            if os.system("ls /usr/local/bin/ | grep aws")==0:
                os.system("tput setaf 3")
                print("AWS CLI is already installed in the system")
            else:
                os.system("tput setaf 3")
                print("Downloading AWS ClI v2....")
                os.system("tput setaf 7")
                if os.system("curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\"") == 0:
                    os.system("tput setaf 3")
                    print("Download successful....\nNow insatlling....")
                    os.system("tput setaf 7")
                    if os.system("unzip awscliv2.zip;sudo ./aws/install")==0:
                        os.system("tput setaf 3")
                        print("AWS CLI installed successfully")
                        os.system("tput setaf 7")
                        os.system("aws --version")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot install the software")
                else:
                    os.system("tput setaf 1")
                    print("Download failed")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==2:
            os.system("tput setaf 4")
            print("logging in.....")
            os.system("tput setaf 7")
            if os.system("aws configure")==0:
                os.system("tput setaf 3")
                print("Logged in")
            else:
                os.system("tput setaf 1")
                print("Cannot login to the account. Please try again")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==3:
            while True:
              os.system("clear")
              os.system("tput setaf 1")
              print("\t\t\t\t\t\t AWS EC2")
              os.system("tput setaf 7")
              print("\t\t\t\t\t--------------------------")

              ec2_menu()
              os.system("tput setaf 3")
              print("\n\t\t\tEnter your Choice : ",end=" ")
              os.system("tput setaf 7")
              x=int(input())

              if x==1:
                  os.system("tput setaf 4")
                  print("Retrieving available instances......")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 describe-instances")==0:
                      os.system("tput setaf 3")
                      print("Success")
                  else:
                      os.system("tput setaf 1")
                      print("Failed to retrieve the information")
                  
                  os.system("tput setaf 2")
                  input("press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
              
              
              elif x==2:
                  os.system("tput setaf 4")
                  print("Enter the name of the key-pair : ")
                  os.system("tput setaf 7")
                  key_name = input()
                  os.system("tput setaf 3")
                  print("Creating key pair...........")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 create-key-pair --key-name %s" %key_name)==0:
                      os.system("tput setaf 3")
                      print("Key pair created successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot create the key")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
              
              
              
              elif x==3:
                  os.system("tput setaf 4")
                  print("Enter the AMI name : ")
                  os.system("tput setaf 7")
                  ami_name = input()
                  ami_id=""
                  if ami_name=="Amazon Linux 2" or ami_name=="amazon linux 2" or ami_name=="AL2" or ami_name=="AmazonLinux2":
                      ami_id = "ami-0e306788ff2473ccb"
                  elif ami_name=="RedHat" or ami_name=="redhat" or ami_name=="red hat" or ami_name=="Red Hat" or ami_name=="RHEL" or ami_name=="rhel":
                      ami_id = "ami-052c08d70def0ac62"
                  elif ami_name=="ubuntu":
                      ami_id = "ami-0cda377a1b884a1bc"
                  
                  os.system("tput setaf 4")
                  print("Enter the Subnet ID: ")
                  os.system("tput setaf 7")
                  subnet_id = input()

                  os.system("tput setaf 4")
                  print("Enter the Instance type: ")
                  os.system("tput setaf 7")
                  instance_type = input()
                  
                  os.system("tput setaf 4")
                  print("Enter the Security Group Name: ")
                  os.system("tput setaf 7")
                  sg_name = input()

                  os.system("tput setaf 3")
                  print("Retrieving the ID......")
                  out = "aws ec2 describe-security-groups --filters Name=group-name,Values=eks_security --query \"SecurityGroups[*].[GroupId]\" --output text"
                  s = os.popen(out).read()
                  sg1 = s.split("\n")
                  sg_id = sg1[0]
                  os.system("tput setaf 4")
                  print("Enter the Key Pair Name: ")
                  os.system("tput setaf 7")
                  key_name = input()

                  os.system("tput setaf 4")
                  print("Count: ")
                  os.system("tput setaf 7")
                  count = input()
                  
                  #print("aws ec2 run-instances --image-id %s --security-group-ids %s --subnet-id %s --instance-type %s --key-name %s --count %s" %(ami_id, sg_id, subnet_id, instance_type, key_name, count))


                  if os.system("aws ec2 run-instances --image-id %s --security-group-ids %s --subnet-id %s --instance-type %s --key-name %s --count %s" %(ami_id, sg_id, subnet_id, instance_type, key_name, count)) == 0:
                      os.system("tput setaf 3")
                      print("Instance Launched successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot launch instance")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")


              elif x==4:
                  os.system("tput setaf 4")
                  print("Enter the instance IDs (Space separated if more than one): ")
                  os.system("tput setaf 7")
                  instance_id = input()
                  os.system("tput setaf 3")
                  print("Stop/Start? : ", end="")
                  os.system("tput setaf 7")
                  ch = input()
                  if ch=="stop" or ch=="Stop" or ch=="STOP":
                      os.system("tput setaf 4")
                      print("Stopping Instance.......")
                      os.system("tput setaf 7")
                      if os.system("aws ec2 stop-instances --instance-ids %s" %instance_id)==0:
                          os.system("tput setaf 3")
                          print("Instances stopped")
                      else:
                          os.system("tput setaf 1")
                          print("Cannot terminate the instances")
                  elif ch=="Start" or ch=="start" or ch=="START":
                      os.system("tput setaf 4")
                      print("Starting Instance.......")
                      os.system("tput setaf 7")
                      if os.system("aws ec2 start-instances --instance-ids %s" %instance_id)==0:
                          os.system("tput setaf 3")
                          print("Instances started")
                      else:
                          os.system("tput setaf 1")
                          print("Cannot start the instances")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==5:
                  os.system("tput setaf 4")
                  print("Enter the instance IDs (Space separated if more than one): ")
                  os.system("tput setaf 7")
                  instance_id = input()
                  os.system("tput setaf 3")
                  print("Terminating Instance.....")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 terminate-instances --instance-ids %s" %instance_id)==0:
                      os.system("tput setaf 3")
                      print("Instance Terminated")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot terminate instance")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
             
              elif x==9:
                  os.system("clear")
                  break
        
        elif choice==4:
            while True:
              os.system("clear")
              os.system("tput setaf 1")
              print("\t\t\t\t\t\t AWS EBS")
              os.system("tput setaf 7")
              print("\t\t\t\t\t--------------------------")

              ebs_menu()
              os.system("tput setaf 3")
              print("\n\t\t\tEnter your Choice : ",end=" ")
              os.system("tput setaf 7")
              x=int(input())

              if x==1:
                  os.system("tput setaf 4")
                  print("Retrieving available Volumes........")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 describe-volumes")==0:
                      os.system("tput setaf 3")
                      print("Success")
                  else:
                      os.system("tput setaf 1")
                      print("Failed to retrieve")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
              
              elif x==2:
                  os.system("tput setaf 4")
                  print("Enter the Availability Zone : ")
                  os.system("tput setaf 7")
                  az = input()
                  os.system("tput setaf 4")
                  print("Enter the size of the volume : ")
                  os.system("tput setaf 7")
                  size = input()
                  os.system("tput setaf 3")
                  print("Creating Volume......")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 create-volume --availability-zone %s --size %s" %(az,size))==0:
                      os.system("tput setaf 3")
                      print("Volume Created")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot create volume")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==3:
                  os.system("tput setaf 4")
                  print("Enter the device name (/dev/sdh or /dev/svdf) : ")
                  os.system("tput setaf 7")
                  device = input()
                  os.system("tput setaf 4")
                  print("Enter the instance ID : ")
                  os.system("tput setaf 7")
                  instance_id = input()
                  os.system("tput setaf 4")
                  print("Enter the volume ID : ")
                  os.system("tput setaf 7")
                  volume_id = input()
                  os.system("tput setaf 3")
                  print("\nAttaching Volume........")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 attach-volume --device %s --volume-id %s --instance-id %s" %(device, volume_id, instance_id))==0:
                      os.system("tput setaf 3")
                      print("Volume attached successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot attach Volume")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==4:
                  os.system("tput setaf 4")
                  print("Enter the Volume IDs (Separate by space if more than one): ")
                  os.system("tput setaf 7")
                  volume_id = input()
                  os.system("tput setaf 3")
                  print("Deleting Volumes......")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 delete-volume --volume-id %s" %volume_id)==0:
                      os.system("tput setaf 3")
                      print("Volume Deleted successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot delete Volume")
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              
              elif x==5:
                  os.system("tput setaf 4")
                  print("Enter snapshot description : ")
                  description = input()

                  os.system("tput setaf 3")
                  print("Retrieving available Snapshots........")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 describe-snapshots --filters Name=description,Values=%s" %description)==0:
                      os.system("tput setaf 3")
                      print("Success")
                  else:
                      os.system("tput setaf 1")
                      print("Failed to retrieve")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              
              elif x==6:
                  os.system("tput setaf 4")
                  print("Enter the Volume ID : ")
                  os.system("tput setaf 7")
                  volume_id = input()
                  os.system("tput setaf 4")
                  print("Enter description : ")
                  os.system("tput setaf 7")
                  description = input()
                  os.system("tput setaf 3")
                  print("Creating Snapshot.........")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 create-snapshot --volume-id %s --description %s" %(volume_id, description))==0:
                      os.system("tput setaf 3")
                      print("Snapshot created successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot create snapshot")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==7:
                  os.system("tput setaf 4")
                  print("Enter the Snapshot ID : ")
                  os.system("tput setaf 7")
                  snapshot_id = input()
                  os.system("tput setaf 3")
                  print("Deleting Snapshot......")
                  os.system("tput setaf 7")
                  if os.system("aws ec2 delete-snapshot --snapshot-id %s" %snapshot_id)==0:
                      os.system("tput setaf 3")
                      print("Snapshot Deleted successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot delete SNapshot")
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")


              elif x==9:
                  os.system("clear")
                  break

        elif choice==5:
            while True:
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\t\t\t\t AWS S3")
                os.system("tput setaf 7")
                print("\t\t\t\t\t--------------------------")

                s3_menu()
                os.system("tput setaf 3")
                print("\n\t\t\tEnter your Choice : ",end=" ")
                os.system("tput setaf 7")
                x=int(input())

                if x==1:
                    os.system("tput setaf 4")
                    print("Retrieving available buckets.........")
                    os.system("tput setaf 7")
                    if os.system("aws s3api list-buckets")==0:
                        os.system("tput setaf 3")
                        print("Success")
                    else:
                        os.system("tput setaf 1")
                        print("Failed to retrieve")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                
                elif x==2:
                    os.system("tput setaf 4")
                    print("Enter the Bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 4")
                    print("Enter the Region : ")
                    os.system("tput setaf 7")
                    region = input()
                    os.system("tput setaf 3")
                    print("Creating Bucket.........")
                    if os.system("aws s3api create-bucket --bucket %s --region %s --create-bucket-configuration LocationConstraint=%s" %(bucket, region,region))==0:
                        os.system("tput setaf 3")
                        print("Bucket created successfully")
                        os.system("tput setaf 7")
                        ch = input("\nDo you want to allow Public access? (y/n) : ")
                        
                        if ch=="y":
                            os.system("tput setaf 4")
                            print("Granting public access........")
                            os.system("tput setaf 7")
                            if os.system("aws s3api put-bucket-acl --acl-public-read --bucket %s" %bucket)==0:
                                os.system("tput setaf 3")
                                print("Bucket is now Public")
                            else:
                                os.system("tput setaf 1")
                                print("Cannot grant public access")

                    else:
                        os.system("tput setaf 1")
                        print("Cannot create bucket")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")
                
                elif x==3:
                    os.system("tput setaf 4")
                    print("Enter the object location : ")
                    os.system("tput setaf 7")
                    object_loc = input()
                    os.system("tput setaf 4")
                    print("Enter the bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 4")
                    print("Enter a unique key to be assigned to the object : ")
                    os.system("tput setaf 7")
                    key = input()
                    os.system("tput setaf 3")
                    print("Uploading object to the Bucket......")
                    if os.system("aws s3api put-object --bucket %s --key %s --body %s" %(bucket, key, object_loc))==0:
                        os.system("tput setaf 3")
                        print("Object uploaded successfully")
                        os.system("tput setaf 7")
                        ch = input("Do you want to make the object public? (y/n) : ")
                        if ch=="y":
                            os.system("tput setaf 4")
                            print("Grantic public readability access.........")
                            os.system("tput setaf 7")
                            if os.system("aws s3api --put-object-acl --bucket %s --key %s --grant-read-url=http://acs.amazonaws.com/groups/global/AllUsers" %(bucket, object_loc))==0:
                                os.system("tput setaf 3")
                                print("Object is now public")
                            else:
                                os.system("tput setaf 1")
                                print("Failed to grant permissions")
                        
                    else:
                        os.system("tput setaf 1")
                        print("Cannot upload object")
                    
                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==4:
                    os.system("tput setaf 4")
                    print("Enter the object key : ")
                    os.system("tput setaf 7")
                    key = input()
                    os.system("tput setaf 4")
                    print("Enter the Bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 3")
                    print("Deleting object..........")
                    os.system("tput setaf 7")
                    if os.system("aws s3api delete-object --bucket %s --key %s" %(bucket, key))==0:
                        os.system("tput setaf 3")
                        print("\nObject deleted succesfully")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot delete object")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==5:
                    os.system("tput setaf 4")
                    print("Enter the Bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 3")
                    print("Deleting bucket........")
                    os.system("tput setaf 7")
                    if os.system("aws s3api delete-bucket --bucket %s" %bucket)==0:
                        os.system("tput setaf 3")
                        print("Bucket deleted successfully")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot delete the bucket")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==9:
                    os.system("clear")
                    break

        elif choice==6:
            while True:
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\t\t\t\t AWS CloudFront")
                os.system("tput setaf 7")
                print("\t\t\t\t\t--------------------------")

                cloudfront_menu()
                os.system("tput setaf 3")
                print("\n\t\t\tEnter your Choice : ",end=" ")
                os.system("tput setaf 7")
                x=int(input())

                if x==1:
                    os.system("tput setaf 4")
                    print("Retrieving available distributions.......")
                    os.system("tput setaf 7")
                    if os.system("aws cloudfront list-distributions")==0:
                        os.system("tput setaf 3")
                        print("Success")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot retrieve distributions")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==2:
                    os.system("tput setaf 4")
                    print("Enter the name of the S3 bucket : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 4")
                    print("Enter the root object location : ")
                    os.system("tput setaf 7")
                    root_object = input()
                    os.system("tput setaf 3")
                    print("Creating distribution........")
                    os.system("tput setaf 7")
                    if os.system("aws cloudfront create-distribution --origin-domain-name %s.s3.amazonaws.com --default-root-object %s" %(bucket,root_object))==0:
                        os.system("tput setaf 3")
                        print("Distribution created successfully")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot create distribution")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==3:
                    os.system("tput setaf 4")
                    print("Enter the distribution ID : ")
                    os.system("tput setaf 7")
                    dist_id = input()
                    os.system("tput setaf 3")
                    print("Deleting distribution")
                    os.system("tput setaf 7")
                    if os.system("aws cloudfront delete-distribution --id %s" %dist_id)==0:
                        os.system("tput setaf 3")
                        print("Distribution deleted successfull")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot delete distribution")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==9:
                    os.system("clear")
                    break

        elif choice==7:
            while True:
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\t\t\t\t AWS IAM")
                os.system("tput setaf 7")
                print("\t\t\t\t\t--------------------------")
                iam_menu()

                os.system("tput setaf 3")
                print("\n\t\t\tEnter your Choice : ",end=" ")
                os.system("tput setaf 7")
                x=int(input())

                if x==1:
                    os.system("tput setaf 4")
                    print("Retrieving available users......")
                    os.system("tput setaf 7")
                    if os.system("aws iam list-users")==0:
                        os.system("tput setaf 3")
                        print("Success")
                    else:
                        os.system("tput setaf 1")
                        print("Failed to retrieve the information")


                    os.system("tput setaf 2")
                    input("press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==2:
                    os.system("tput setaf 4")
                    print("Enter the user name you want to create : ")
                    os.system("tput setaf 7")
                    cun = input()
                    if os.system("aws iam create-user --user-name %s" %cun)==0:
                        os.system("tput setaf 3")
                        print("User Created")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot create user")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")


                elif x==3:
                    os.system("tput setaf 4")
                    print("Enter the user name you want to delete : ")
                    os.system("tput setaf 7")
                    dun = input()
                    if os.system("aws iam delete-user --user-name %s" %dun)==0:
                        os.system("tput setaf 3")
                        print("User Deleted")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot deleted user")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==9:
                    os.system("clear")
                    break


    elif loc=="remote":
        if choice==1:
            os.system("tput setaf 4")
            print("Validating......")
            os.system("tput setaf 7")
            if os.system("ssh %s ls /usr/local/bin/ | grep aws" %ip)==0:
                os.system("tput setaf 3")
                print("AWS CLI is already installed in the system")
            else:
                os.system("tput setaf 3")
                print("Downloading AWS ClI v2....")
                os.system("tput setaf 7")
                if os.system("ssh %s curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\"" %ip) == 0:
                    os.system("tput setaf 3")
                    print("Download successful....\nNow insatlling....")
                    os.system("tput setaf 7")
                    if os.system("ssh %s unzip awscliv2.zip;sudo ./aws/install" %ip)==0:
                        os.system("tput setaf 3")
                        print("AWS CLI installed successfully")
                        os.system("tput setaf 7")
                        os.system("ssh %s aws --version" %ip)
                    else:
                        os.system("tput setaf 1")
                        print("Cannot install the software")
                else:
                    os.system("tput setaf 1")
                    print("Download failed")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==2:
            os.system("tput setaf 4")
            print("logging in.....")
            os.system("tput setaf 7")
            if os.system("ssh %s aws configure" %ip)==0:
                os.system("tput setaf 3")
                print("Logged in")
            else:
                os.system("tput setaf 1")
                print("Cannot login to the account. Please try again")

            os.system("tput setaf 2")
            input("Press any key to continue")
            os.system("tput setaf 7")
            os.system("clear")

        elif choice==3:
            while True:
              os.system("clear")
              os.system("tput setaf 1")
              print("\t\t\t\t\t\t AWS EC2")
              os.system("tput setaf 7")
              print("\t\t\t\t\t--------------------------")

              ec2_menu()
              os.system("tput setaf 3")
              print("\n\t\t\tEnter your Choice : ",end=" ")
              os.system("tput setaf 7")
              x=int(input())

              if x==1:
                  os.system("tput setaf 4")
                  print("Retrieving available instances......")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 describe-instances" %ip)==0:
                      os.system("tput setaf 3")
                      print("Success")
                  else:
                      os.system("tput setaf 1")
                      print("Failed to retrieve the information")
                  
                  os.system("tput setaf 2")
                  input("press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
              
              elif x==2:
                  os.system("tput setaf 4")
                  print("Enter the name of the key-pair : ")
                  os.system("tput setaf 7")
                  key_name = input()
                  os.system("tput setaf 3")
                  print("Creating key pair...........")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 create-key-pair --key-name %s" %(remoteip, key_name))==0:
                      os.system("tput setaf 3")
                      print("Key pair created successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot create the key")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
              
              
              elif x==3:
                  os.system("tput setaf 4")
                  print("Enter the AMI name : ")
                  os.system("tput setaf 7")
                  ami_name = input()
                  ami_id=""
                  if ami_name=="Amazon Linux 2" or ami_name=="amazon linux 2" or ami_name=="AL2" or ami_name=="AmazonLinux2":
                      ami_id = "ami-0e306788ff2473ccb"
                  elif ami_name=="RedHat" or ami_name=="redhat" or ami_name=="red hat" or ami_name=="Red Hat" or ami_name=="RHEL" or ami_name=="rhel":
                      ami_id = "ami-052c08d70def0ac62"
                  elif ami_name=="ubuntu":
                      ami_id = "ami-0cda377a1b884a1bc"
                  
                  os.system("tput setaf 4")
                  print("Enter the Subnet ID: ")
                  os.system("tput setaf 7")
                  subnet_id = input()

                  os.system("tput setaf 4")
                  print("Enter the Instance type: ")
                  os.system("tput setaf 7")
                  instance_type = input()
                  
                  os.system("tput setaf 4")
                  print("Enter the Security Group Name: ")
                  os.system("tput setaf 7")
                  sg_name = input()

                  os.system("tput setaf 3")
                  print("Retrieving the ID......")
                  out = "aws ec2 describe-security-groups --filters Name=group-name,Values=eks_security --query \"SecurityGroups[*].[GroupId]\" --output text"
                  s = os.popen(out).read()
                  sg1 = s.split("\n")
                  sg_id = sg1[0]
                  os.system("tput setaf 4")
                  print("Enter the Key Pair Name: ")
                  os.system("tput setaf 7")
                  key_name = input()

                  os.system("tput setaf 4")
                  print("Count: ")
                  os.system("tput setaf 7")
                  count = input()
                  
                  #print("aws ec2 run-instances --image-id %s --security-group-ids %s --subnet-id %s --instance-type %s --key-name %s --count %s" %(ami_id, sg_id, subnet_id, instance_type, key_name, count))


                  if os.system("ssh %s aws ec2 run-instances --image-id %s --security-group-ids %s --subnet-id %s --instance-type %s --key-name %s --count %s" %(ip, ami_id, sg_id, subnet_id, instance_type, key_name, count)) == 0:
                      os.system("tput setaf 3")
                      print("Instance Launched successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot launch instance")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")


              elif x==4:
                  os.system("tput setaf 4")
                  print("Enter the instance IDs (Space separated if more than one): ")
                  os.system("tput setaf 7")
                  instance_id = input()
                  os.system("tput setaf 3")
                  print("Stop/Start? : ", end="")
                  os.system("tput setaf 7")
                  ch = input()
                  if ch=="stop" or ch=="Stop" or ch=="STOP":
                      os.system("tput setaf 4")
                      print("Stopping Instance.......")
                      os.system("tput setaf 7")
                      if os.system("ssh %s aws ec2 stop-instances --instance-ids %s" %(ip, instance_id))==0:
                          os.system("tput setaf 3")
                          print("Instances stopped")
                      else:
                          os.system("tput setaf 1")
                          print("Cannot terminate the instances")
                  elif ch=="Start" or ch=="start" or ch=="START":
                      os.system("tput setaf 4")
                      print("Starting Instance.......")
                      os.system("tput setaf 7")
                      if os.system("ssh %s aws ec2 start-instances --instance-ids %s" %(ip, instance_id))==0:
                          os.system("tput setaf 3")
                          print("Instances started")
                      else:
                          os.system("tput setaf 1")
                          print("Cannot start the instances")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==5:
                  os.system("tput setaf 4")
                  print("Enter the instance IDs (Space separated if more than one): ")
                  os.system("tput setaf 7")
                  instance_id = input()
                  os.system("tput setaf 3")
                  print("Terminating Instance.....")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 terminate-instances --instance-ids %s" %(ip, instance_id))==0:
                      os.system("tput setaf 3")
                      print("Instance Terminated")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot terminate instance")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
             
              elif x==9:
                  os.system("clear")
                  break
        
        elif choice==4:
            while True:
              os.system("clear")
              os.system("tput setaf 1")
              print("\t\t\t\t\t\t AWS EBS")
              os.system("tput setaf 7")
              print("\t\t\t\t\t--------------------------")

              ebs_menu()
              os.system("tput setaf 3")
              print("\n\t\t\tEnter your Choice : ",end=" ")
              os.system("tput setaf 7")
              x=int(input())

              if x==1:
                  os.system("tput setaf 4")
                  print("Retrieving available Volumes........")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 describe-volumes" %ip)==0:
                      os.system("tput setaf 3")
                      print("Success")
                  else:
                      os.system("tput setaf 1")
                      print("Failed to retrieve")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
              
              elif x==2:
                  os.system("tput setaf 4")
                  print("Enter the Availability Zone : ")
                  os.system("tput setaf 7")
                  az = input()
                  os.system("tput setaf 4")
                  print("Enter the size of the volume : ")
                  os.system("tput setaf 7")
                  size = input()
                  os.system("tput setaf 3")
                  print("Creating Volume......")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 create-volume --availability-zone %s --size %s" %(ip,az,size))==0:
                      os.system("tput setaf 3")
                      print("Volume Created")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot create volume")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==3:
                  os.system("tput setaf 4")
                  print("Enter the device name (/dev/sdh or /dev/svdf) : ")
                  os.system("tput setaf 7")
                  device = input()
                  os.system("tput setaf 4")
                  print("Enter the instance ID : ")
                  os.system("tput setaf 7")
                  instance_id = input()
                  os.system("tput setaf 4")
                  print("Enter the volume ID : ")
                  os.system("tput setaf 7")
                  volume_id = input()
                  os.system("tput setaf 3")
                  print("\nAttaching Volume........")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 attach-volume --device %s --volume-id %s --instance-id %s" %(ip, device, volume_id, instance_id))==0:
                      os.system("tput setaf 3")
                      print("Volume attached successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot attach Volume")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==4:
                  os.system("tput setaf 4")
                  print("Enter the Volume IDs (Separate by space if more than one): ")
                  os.system("tput setaf 7")
                  volume_id = input()
                  os.system("tput setaf 3")
                  print("Deleting Volumes......")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 delete-volume --volume-id %s" %(ip, volume_id))==0:
                      os.system("tput setaf 3")
                      print("Volume Deleted successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot delete Volume")
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              
              elif x==5:
                  os.system("tput setaf 4")
                  print("Enter snapshot description : ")
                  description = input()

                  os.system("tput setaf 3")
                  print("Retrieving available Snapshots........")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 describe-snapshots --filters Name=description,Values=%s" %(ip,description))==0:
                      os.system("tput setaf 3")
                      print("Success")
                  else:
                      os.system("tput setaf 1")
                      print("Failed to retrieve")

                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              
              elif x==6:
                  os.system("tput setaf 4")
                  print("Enter the Volume ID : ")
                  os.system("tput setaf 7")
                  volume_id = input()
                  os.system("tput setaf 4")
                  print("Enter description : ")
                  os.system("tput setaf 7")
                  description = input()
                  os.system("tput setaf 3")
                  print("Creating Snapshot.........")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 create-snapshot --volume-id %s --description %s" %(ip,volume_id, description))==0:
                      os.system("tput setaf 3")
                      print("Snapshot created successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot create snapshot")
                  
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")

              elif x==7:
                  os.system("tput setaf 4")
                  print("Enter the Snapshot ID : ")
                  os.system("tput setaf 7")
                  snapshot_id = input()
                  os.system("tput setaf 3")
                  print("Deleting Snapshot......")
                  os.system("tput setaf 7")
                  if os.system("ssh %s aws ec2 delete-snapshot --snapshot-id %s" %(ip,snapshot_id))==0:
                      os.system("tput setaf 3")
                      print("Snapshot Deleted successfully")
                  else:
                      os.system("tput setaf 1")
                      print("Cannot delete SNapshot")
                  os.system("tput setaf 2")
                  input("Press any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")


              elif x==9:
                  os.system("clear")
                  break

        elif choice==5:
            while True:
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\t\t\t\t AWS S3")
                os.system("tput setaf 7")
                print("\t\t\t\t\t--------------------------")

                s3_menu()
                os.system("tput setaf 3")
                print("\n\t\t\tEnter your Choice : ",end=" ")
                os.system("tput setaf 7")
                x=int(input())

                if x==1:
                    os.system("tput setaf 4")
                    print("Retrieving available buckets.........")
                    os.system("tput setaf 7")
                    if os.system("ssh %s aws s3api list-buckets" %ip)==0:
                        os.system("tput setaf 3")
                        print("Success")
                    else:
                        os.system("tput setaf 1")
                        print("Failed to retrieve")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                
                elif x==2:
                    os.system("tput setaf 4")
                    print("Enter the Bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 4")
                    print("Enter the Region : ")
                    os.system("tput setaf 7")
                    region = input()
                    os.system("tput setaf 3")
                    print("Creating Bucket.........")
                    if os.system("ssh %s aws s3api create-bucket --bucket %s --region %s --create-bucket-configuration LocationConstraint=%s" %(ip,bucket, region,region))==0:
                        os.system("tput setaf 3")
                        print("Bucket created successfully")
                        os.system("tput setaf 7")
                        ch = input("\nDo you want to allow Public access? (y/n) : ")
                        
                        if ch=="y":
                            os.system("tput setaf 4")
                            print("Granting public access........")
                            os.system("tput setaf 7")
                            if os.system("ssh %s aws s3api put-bucket-acl --acl-public-read --bucket %s" %(ip,bucket))==0:
                                os.system("tput setaf 3")
                                print("Bucket is now Public")
                            else:
                                os.system("tput setaf 1")
                                print("Cannot grant public access")

                    else:
                        os.system("tput setaf 1")
                        print("Cannot create bucket")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")
                
                elif x==3:
                    os.system("tput setaf 4")
                    print("Enter the object location : ")
                    os.system("tput setaf 7")
                    object_loc = input()
                    os.system("tput setaf 4")
                    print("Enter the bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 4")
                    print("Enter a unique key to be assigned to the object : ")
                    os.system("tput setaf 7")
                    key = input()
                    os.system("tput setaf 3")
                    print("Uploading object to the Bucket......")
                    if os.system("ssh %s aws s3api put-object --bucket %s --key %s --body %s" %(ip,bucket, key, object_loc))==0:
                        os.system("tput setaf 3")
                        print("Object uploaded successfully")
                        os.system("tput setaf 7")
                        ch = input("Do you want to make the object public? (y/n) : ")
                        if ch=="y":
                            os.system("tput setaf 4")
                            print("Grantic public readability access.........")
                            os.system("tput setaf 7")
                            if os.system("ssh %s aws s3api --put-object-acl --bucket %s --key %s --grant-read-url=http://acs.amazonaws.com/groups/global/AllUsers" %(ip,bucket, object_loc))==0:
                                os.system("tput setaf 3")
                                print("Object is now public")
                            else:
                                os.system("tput setaf 1")
                                print("Failed to grant permissions")
                        
                    else:
                        os.system("tput setaf 1")
                        print("Cannot upload object")
                    
                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==4:
                    os.system("tput setaf 4")
                    print("Enter the object key : ")
                    os.system("tput setaf 7")
                    key = input()
                    os.system("tput setaf 4")
                    print("Enter the Bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 3")
                    print("Deleting object..........")
                    os.system("tput setaf 7")
                    if os.system("ssh %s aws s3api delete-object --bucket %s --key %s" %(ip,bucket, key))==0:
                        os.system("tput setaf 3")
                        print("\nObject deleted succesfully")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot delete object")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==5:
                    os.system("tput setaf 4")
                    print("Enter the Bucket name : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 3")
                    print("Deleting bucket........")
                    os.system("tput setaf 7")
                    if os.system("ssh %s aws s3api delete-bucket --bucket %s" %(ip,bucket))==0:
                        os.system("tput setaf 3")
                        print("Bucket deleted successfully")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot delete the bucket")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==9:
                    os.system("clear")
                    break

        elif choice==6:
            while True:
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\t\t\t\t AWS CloudFront")
                os.system("tput setaf 7")
                print("\t\t\t\t\t--------------------------")

                cloudfront_menu()
                os.system("tput setaf 3")
                print("\n\t\t\tEnter your Choice : ",end=" ")
                os.system("tput setaf 7")
                x=int(input())

                if x==1:
                    os.system("tput setaf 4")
                    print("Retrieving available distributions.......")
                    os.system("tput setaf 7")
                    if os.system("ssh %s aws cloudfront list-distributions" %ip)==0:
                        os.system("tput setaf 3")
                        print("Success")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot retrieve distributions")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==2:
                    os.system("tput setaf 4")
                    print("Enter the name of the S3 bucket : ")
                    os.system("tput setaf 7")
                    bucket = input()
                    os.system("tput setaf 4")
                    print("Enter the root object location : ")
                    os.system("tput setaf 7")
                    root_object = input()
                    os.system("tput setaf 3")
                    print("Creating distribution........")
                    os.system("tput setaf 7")
                    if os.system("ssh %s aws cloudfront create-distribution --origin-domain-name %s.s3.amazonaws.com --default-root-object %s" %(ip, bucket,root_object))==0:
                        os.system("tput setaf 3")
                        print("Distribution created successfully")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot create distribution")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==3:
                    os.system("tput setaf 4")
                    print("Enter the distribution ID : ")
                    os.system("tput setaf 7")
                    dist_id = input()
                    os.system("tput setaf 3")
                    print("Deleting distribution")
                    os.system("tput setaf 7")
                    if os.system("ssh %s aws cloudfront delete-distribution --id %s" %(ip,dist_id))==0:
                        os.system("tput setaf 3")
                        print("Distribution deleted successfull")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot delete distribution")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==9:
                    os.system("clear")
                    break

        elif choice==7:
            while True:
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\t\t\t\t AWS IAM")
                os.system("tput setaf 7")
                print("\t\t\t\t\t--------------------------")
                iam_menu()

                os.system("tput setaf 3")
                print("\n\t\t\tEnter your Choice : ",end=" ")
                os.system("tput setaf 7")
                x=int(input())

                if x==1:
                    os.system("tput setaf 4")
                    print("Retrieving available users......")
                    os.system("tput setaf 7")
                    if os.system("ssh %s aws iam list-users" %ip)==0:
                        os.system("tput setaf 3")
                        print("Success")
                    else:
                        os.system("tput setaf 1")
                        print("Failed to retrieve the information")


                    os.system("tput setaf 2")
                    input("press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==2:
                    os.system("tput setaf 4")
                    print("Enter the user name you want to create : ")
                    os.system("tput setaf 7")
                    cun = input()
                    if os.system("ssh %s aws iam create-user --user-name %s" %(ip,cun))==0:
                        os.system("tput setaf 3")
                        print("User Created")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot create user")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")


                elif x==3:
                    os.system("tput setaf 4")
                    print("Enter the user name you want to delete : ")
                    os.system("tput setaf 7")
                    dun = input()
                    if os.system("ssh %s aws iam delete-user --user-name %s" %(ip,dun))==0:
                        os.system("tput setaf 3")
                        print("User Deleted")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot deleted user")

                    os.system("tput setaf 2")
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                    os.system("clear")

                elif x==9:
                    os.system("clear")
                    break



def ec2_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: Describe running instances
             \t\t Press 2: Create a key pair
             \t\t Press 3: Launch an instance
             \t\t Press 4: Stop/Start an instance
             \t\t Press 5: Terminate an instance
             \t\t Press 9: Back""")
    print("\t\t####################################################################")

def ebs_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: List available volumes
             \t\t Press 2: Create a new volume
             \t\t Press 3: Attach volume to an EC2 instance
             \t\t Press 4: Delete a volume
             \t\t Press 5: List available Snapshots
             \t\t Press 6: Create Snapshot
             \t\t Press 7: Delete Snapshot
             \t\t Press 9: Back""")
    print("\t\t####################################################################")

def s3_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: List Buckets
             \t\t Press 2: Create a new bucket
             \t\t Press 3: Add object to a bucket
             \t\t Press 4: Delete an object
             \t\t Press 5: Delete a Bucket
             \t\t Press 9: Back""")
    print("\t\t####################################################################")


def cloudfront_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: List distributions
             \t\t Press 2: Create a Distribution
             \t\t Press 3: Delete a Distribution
             \t\t Press 9: Back""")
    print("\t\t####################################################################")



def iam_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: List users
             \t\t Press 2: Create a user
             \t\t Press 3: Delete an existing user
             \t\t Press 9: Back""")
    print("\t\t####################################################################")




