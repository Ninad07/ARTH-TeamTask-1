import os
import getpass
from aws import aws_menu
from aws import ec2_menu
from aws import aws_functions
from docker import docker_menu
from docker import docker_functions

#Hadoop Menu
def hadoop_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: Configure the Hadoop Server
             \t\t Press 2: Start Hadoop Services
             \t\t Press 3: Cluster Report
             \t\t Press 4: List the files uploaded in the cluster
             \t\t Press 5: Read a file from the cluster
             \t\t Press 6: Upload a file into the cluster
             \t\t Press 7: Stop Hadoop Services
             \t\t Press 9: Back
             \t\t Press 0: Exit""")
    print("\t\t####################################################################")


#LVM menu
def lvm_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: Check available disks
             \t\t Press 2: Create Physical Volumes(PV)
             \t\t Press 3: Create Volume Groups(VG)
             \t\t Press 4: Create Logical Volumes(LV)
             \t\t Press 5: Mount the LV
             \t\t Press 6: Extend Volume Group
             \t\t Press 7: Extend Logical Volume
             \t\t Press 8: Display
             \t\t Press 9: Back
             \t\t Press 0: Exit""")
    print("\t\t####################################################################")

#Display
def display():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: Display Physical Volumes(PV)
             \t\t Press 2: Display Volume Groups(VG)
             \t\t Press 3: Display Logical Volumes(LV)
             \t\t Press 4: Display mounted directories
             \t\t Press 0: Back""")
    print("\t\t####################################################################")


#Main Menu
def main_menu():
    print("\n\t\t####################################################################")
    print("""\t\t\t Press 1: AWS
             \t\t Press 2: Hadoop
             \t\t Press 3: Docker
             \t\t Press 4: LVM Partitions
             \t\t Press 0: Exit""")
    print("\t\t####################################################################")


def hadoop_hdfs_conf(node, location):
    if location == "remote":
      if node == "namenode" or node == "Namenode" or node == "NameNode" or node == "NAMENODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
          master_dir = input("Enter the directory you want to assign for the Namenode : ")
          os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml" %master_dir)
          os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
          os.system("scp /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml" %remoteip) 
    
      elif node == "datanode" or node == "Datanode" or node == "DataNode" or node == "DATANODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
          slave_dir = input("Enter the directory you want to assign for the Datanode : ")
          os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml" %slave_dir)
          os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
          os.system("scp /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml" %remoteip)
    
    elif location == "local":
      if node == "namenode" or node == "Namenode" or node == "NameNode" or node == "NAMENODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
          master_dir = input("Enter the directory you want to assign for the Namenode : ")
          os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml" %master_dir)
          os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
    
      elif node == "datanode" or node == "Datanode" or node == "DataNode" or node == "DATANODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
          slave_dir = input("Enter the directory you want to assign for the Datanode : ")
          os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml" %slave_dir)
          os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")


def hadoop_core_conf(node, location):
    if location == "remote":
      if node == "namenode" or node == "Namenode" or node == "NameNode" or node == "NAMENODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
          cluster_port = input("Enter the port number : ") 
          os.system("echo '<value>hdfs://0.0.0.0:%s</value>' >> /etc/hadoop/core-site.xml" %cluster_port)
          os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
          os.system("scp /etc/hadoop/core-site.xml 'root@%s':/etc/hadoop/core-site.xml" %remoteip)
    
      elif node == "datanode" or node == "Datanode" or node == "DataNode" or node == "DATANODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
          master_ip = input("Enter the IP of the Namenode : ")
          cluster_port = input("Enter the port number : ")
          os.system("echo '<value>hdfs://%s:%s</value>' >> /etc/hadoop/core-site.xml" %(master_ip, cluster_port))
          os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
          os.system("scp /etc/hadoop/core-site.xml 'root@%s':/etc/hadoop/core-site.xml" %remoteip)

    elif location == "local":
      if node == "namenode" or node == "Namenode" or node == "NameNode" or node == "NAMENODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
          cluster_port = input("Enter the port number : ")
          os.system("echo '<value>hdfs://0.0.0.0:%s</value>' >> /etc/hadoop/core-site.xml" %cluster_port)
          os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")

      elif node == "datanode" or node == "Datanode" or node == "DataNode" or node == "DATANODE":
          os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
          os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
          os.system("echo ' ' >> /etc/hadoop/core-site.xml")
          os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
          master_ip = input("Enter the IP of the Namenode : ")
          cluster_port = input("Enter the port number : ")
          os.system("echo '<value>hdfs://%s:%s</value>' >> /etc/hadoop/core-site.xml" %(master_ip, cluster_port))
          os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
          os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")



os.system("clear")
os.system("tput setaf 1")
print("\t\t\t\t\t\t Welcome")
os.system("tput setaf 7")
print("\t\t\t\t\t--------------------------")

#To set password
i=0
while i<2:
    passwd = getpass.getpass("Enter the Password : ")
    apass = "Pass@123"
    if passwd==apass:
        os.system("tput setaf 4")
        print("Logged in successfully")
        os.system("tput setaf 7")
        break
    else:
        os.system("tput setaf 1")
        print("Wrong Password. Please retry")
        os.system("tput setaf 7")
    i+=1
else:
    os.system("tput setaf 1")
    print("Authentication failed\nexiting........")
    os.system("tput setaf 7")
    os.system("sleep 1")
    exit()


#Task Location
while True:
    print("Select your Task location (local/remote): ",end=' ')
    location=input()

    if location=="local" or location=="remote":
        break
    else:
        print("Invalid Location!")
    i+=1
    



if location=="remote":
    os.system("tput setaf 3")
    print("Enter the remote IP address : ")
    os.system("tput setaf 7")
    remoteip=input()
    #os.system("tput setaf 3")
    os.system("ssh-keygen")
    os.system("tput setaf 3")
    os.system("ssh-copy-id %s" %remoteip)
    os.system("tput setaf 7")
    input("Press any key to continue")


z=0
while True:
    if z==0:
        z=1
    else:
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t Controller")
        os.system("tput setaf 7")
        print("\t\t\t\t\t--------------------------")

    os.system("clear")
    while True:
      os.system("clear")
      os.system("tput setaf 1")
      print("\t\t\t\t\t\t Controller")
      os.system("tput setaf 7")
      print("\t\t\t\t\t--------------------------")

      main_menu()
      os.system("tput setaf 3")
      print("\n\t\t\tEnter your Choice : ",end=" ")
      os.system("tput setaf 7")
      y=int(input())
      
      if y==4:
        while True:
          os.system("clear")
          os.system("tput setaf 1")
          print("\t\t\t\t\t\t LVM")
          os.system("tput setaf 7")
          print("\t\t\t\t\t--------------------------")

          lvm_menu()
          os.system("tput setaf 3")
          print("\n\t\t\tEnter your Choice : ",end=" ")
          os.system("tput setaf 7")
          x=int(input())
            
          if location == "local":
            if x==1:
              os.system("tput setaf 4")
              print("Checking available disks......\n")
              os.system("tput setaf 7")
              os.system("fdisk -l")
              print()
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")

            elif x==2:
              os.system("tput setaf 4")
              print("Enter the Disk name : ")
              os.system("tput setaf 7")
              disk_name = input()
              os.system("tput setaf 2")
              print("Creating Physical Volume....")
              os.system("tput setaf 7")
              if os.system("pvcreate %s" %disk_name)==0:
                os.system("tput setaf 3")
                print("Physical Volume created")
                print()
                os.system("tput setaf 2")
                input("Press any key to continue")
                os.system("tput setaf 7")
              else:
                os.system("tput setaf 1")
                print("Cannot create Physical Volume")
                print()
                os.system("tput setaf 2")
                input("Press any key to continue")
                os.system("tput setaf 7")
                os.system("clear")

            elif x==3:
              os.system("tput setaf 4")
              print("Enter the name of the VG to be created : ")
              os.system("tput setaf 7")
              vg_name = input()
              os.system("tput setaf 4")
              print("Enter the PVs(Separate by space if more than one) : ")
              os.system("tput setaf 7")
              pv_names = input()
              os.system("tput setaf 2")
              print("Creating Volume Group.....\n")
              os.system("tput setaf 7")
              if os.system("vgcreate %s %s" %(vg_name, pv_names))==0:
                os.system("tput setaf 3")
                print("Volume Group created")
                os.system("tput setaf 7")
                print()
                os.system("tput setaf 2")
                input("Press any key to continue")
                os.system("tput setaf 7")
              else:
                os.system("tput setaf 1")
                print("Cannot create Volume Group")
                os.system("tput setaf 2")
                print()
                input("Press any key to continue")
                os.system("tput setaf 7")
                os.system("clear")

            elif x==4:
              os.system("tput setaf 4")
              print("Enter the size of the partition : ")
              os.system("tput setaf 7")
              size = input()
              os.system("tput setaf 4")
              print("Enter the name of the LV to be created : ")
              os.system("tput setaf 7")
              lv_name = input()
              os.system("tput setaf 4")
              print("Enter the VG to be used: ")
              os.system("tput setaf 7")
              vg_name = input()
              os.system("tput setaf 3")
              print("Creating Logical Volume........")
              os.system("tput setaf 7")
              if os.system("lvcreate --size +%sG --name %s %s" %(size, lv_name, vg_name)) == 0:
                  os.system("tput setaf 3")
                  print("Logical Volume %s has been created" %lv_name)
                  os.system("tput setaf 2")
                  print()
                  input("Press any key to continue")
                  os.system("tput setaf 7")
              else:
                  os.system("tput setaf 1")
                  print("Cannot create LV")
                  os.system("tput setaf 2")
                  print()
                  input("Press any key to continue")
                  os.system("tput setaf 7")
              os.system("clear")

            elif x==5:
                os.system("tput setaf 4")
                print("Enter the name of the LV to be mounted: ")
                os.system("tput setaf 7")
                lv_name = input()
                os.system("tput setaf 4")
                print("Enter the directory location : ")
                os.system("tput setaf 7")
                dir_name = input()
                os.system("tput setaf 3")
                print("Formatting volume.....")
                os.system("tput setaf 7")
                if os.system("mkfs.ext4 %s" %lv_name)==0:
                    os.system("tput setaf 3")
                    print("LV formatted\n")
                    os.system("tput setaf 3")
                    print("Mounting Volume.......")
                    os.system("tput setaf 7")
                    if os.system("mount %s %s" %(lv_name, dir_name)) == 0:
                      os.system("tput setaf 3")
                      print("LV has been mounted on %s" %dir_name)
                      os.system("tput setaf 2")
                      print()
                      input("Press any key to continue")
                      os.system("tput setaf 7")
                    else:
                      os.system("tput setaf 1")
                      print("Cannot mount volume. Please recheck the directory")
                      os.system("tput setaf 2")
                      print()
                      input("Press any key to continue")
                      os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot format the volume")
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                os.system("clear")
            
            elif x==6:
                os.system("tput setaf 4")
                print("Enter the VG name to be extended : ")
                os.system("tput setaf 7")
                vg_name = input()
                os.system("tput setaf 4")
                print("Enter the disk names to be appended(Separate by space if more than one) : ")
                os.system("tput setaf 7")
                disk_names = input()
                os.system("tput setaf 3")
                print("Extending the Volume Group......")
                os.system("tput setaf 7")
                if os.system("vgextend %s %s" %(vg_name, disk_names))==0:
                    os.system("tput setaf 3")
                    print("Volume Group %s extended" %vg_name)
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot extend VG")
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                os.system("clear")

            elif x==7:
                os.system("tput setaf 4")
                print("Enter the name of the LV to be extended : ")
                os.system("tput setaf 7")
                lv_name = input()
                os.system("tput setaf 4")
                print("Enter the size of extension : ")
                os.system("tput setaf 7")
                size = input()
                os.system("tput setaf 3")
                print("Extending the Logical Volume....")
                os.system("tput setaf 7")
                if os.system("lvextend --size +%sG %s" %(size, lv_name))==0:
                    os.system("tput setaf 3")
                    print("Resizing the partition......")
                    os.system("tput setaf 7")
                    if os.system("resize2fs %s" %lv_name)==0:
                        os.system("tput setaf 3")
                        print("Logical Volume %s has been extended successfully" %lv_name)
                        os.system("tput setaf 2")
                        print()
                        input("Press any key to continue")
                        os.system("tput setaf 7")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot resize the partition. Volume remains unextended")
                        os.system("tput setaf 2")
                        print()
                        input("Press any key to continue")
                        os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot extend the volume")
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                os.system("clear")

            elif x==8:
                os.system("clear")
                
                while True:
                    os.system("tput setaf 1")
                    print("\t\t\t\t\t\t Display")
                    os.system("tput setaf 7")
                    print("\t\t\t\t\t--------------------------")
                    display()
                    os.system("tput setaf 3")
                    print("\n\t\t\tEnter your Choice : ",end=" ")
                    os.system("tput setaf 7")
                    d=int(input())

                    if d==1:
                        os.system("tput setaf 7")
                        display_all = input("Do you want to display the info of all PVs? (y/n) : ")
                        if display_all=="y":
                            os.system("tput setaf 3")
                            print("Displaying available Physical Volumes.....")
                            os.system("tput setaf 7")
                            os.system("pvdisplay")
                            os.system("tput setaf 2")
                            print()
                            input("Press eny key to continue")
                            os.system("tput setaf 7")

                        else:
                            os.system("tput setaf 4")
                            print("Enter the name of the PV to be displayed : ")
                            os.system("tput setaf 7")
                            pv_name = input()
                            os.system("tput setaf 3")
                            print("Displaying Physical Volume %s......." %pv_name)
                            os.system("tput setaf 7")
                            os.system("pvdisplay %s" %pv_name)
                            os.system("tput setaf 2")
                            print()
                            input("Press any key to continue")
                            os.system("tput setaf 7")
                        os.system("clear")
                            
                    elif d==2:
                        os.system("tput setaf 7")
                        display_all = input("Do you want to display the info of all VGs? (y/n) : ")
                        if display_all=="y":
                            os.system("tput setaf 3")
                            print("Displaying available Volume Groups.....")
                            os.system("tput setaf 7")
                            os.system("vgdisplay")
                            os.system("tput setaf 2")
                            print()
                            input("Press eny key to continue")
                            os.system("tput setaf 7")
                        else:
                            os.system("tput setaf 4")
                            print("Enter the name of the VG to be displayed : ")
                            os.system("tput setaf 7")
                            vg_name = input()
                            os.system("tput setaf 3")
                            print("Displaying Volume Group %s......." %vg_name)
                            os.system("tput setaf 7")
                            os.system("vgdisplay %s" %vg_name)
                            os.system("tput setaf 2")
                            print()
                            input("Press any key to continue")
                            os.system("tput setaf 7")
                        os.system("clear")

                    elif d==3:
                        os.system("tput setaf 7")
                        display_all = input("Do you want to display the info of all LVs? (y/n) : ")
                        if display_all=="y":
                            os.system("tput setaf 3")
                            print("Displaying available Logical Volumes.....")
                            os.system("tput setaf 7")
                            os.system("lvdisplay")
                            os.system("tput setaf 2")
                            print()
                            input("Press eny key to continue")
                            os.system("tput setaf 7")
                        else:
                            os.system("tput setaf 4")
                            print("Enter the name of the LV to be displayed : ")
                            os.system("tput setaf 7")
                            lv_name = input()
                            os.system("tput setaf 3")
                            print("Displaying Logical Volume %s......." %lv_name)
                            os.system("tput setaf 7")
                            os.system("lvdisplay %s" %lv_name)
                            os.system("tput setaf 2")
                            print()
                            input("Press any key to continue")
                            os.system("tput setaf 7")
                        os.system("clear")

                    elif d==4:
                        os.system("tput setaf 3")
                        print("Displaying the mounted directories......")
                        os.system("tput setaf 7")
                        os.system("df -hT")
                        os.system("tput setaf 2")
                        print()
                        input("Press any key to continue")
                        os.system("tput setaf 7")
                        os.system("clear")

                    elif d==0:
                        os.system("clear")
                        break

                    else:
                      os.system("tput setaf 1")
                      print("=>Option not supported!")
                      os.system("tput setaf 2")
                      input("Press any key to continue")
                      os.system("clear")

            elif x==9:
              os.system("clear")
              break

            elif x==0:
              os.system("tput setaf 1")
              print("=>Exiting.....")
              os.system("tput setaf 7")
              os.system("sleep 1")
              os.system("clear")
              exit()

            else:
              os.system("tput setaf 1")
              print("=>Option not supported!")
              os.system("tput setaf 2")

              input("Press any key to continue")
              os.system("clear")
              os.system("tput setaf 1")
              print("\t\t\t\t\t\t LVM")
              os.system("tput setaf 7")
              print("\t\t\t\t\t--------------------------")
	
          elif location == "remote":
            if x==1:
              os.system("tput setaf 4")
              print("Checking available disks......\n")
              os.system("tput setaf 7")
              os.system("ssh %s fdisk -l" %remoteip)
              print()
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")

            elif x==2:
              os.system("tput setaf 4")
              print("Enter the Disk name : ")
              os.system("tput setaf 7")
              disk_name = input()
              os.system("tput setaf 2")
              print("Creating Physical Volume....")
              os.system("tput setaf 7")
              if os.system("ssh %s pvcreate %s" %(remoteip, disk_name))==0:
                os.system("tput setaf 3")
                print("Physical Volume created")
                print()
                os.system("tput setaf 2")
                input("Press any key to continue")
                os.system("tput setaf 7")
              else:
                os.system("tput setaf 1")
                print("Cannot create Physical Volume")
                print()
                os.system("tput setaf 2")
                input("Press any key to continue")
                os.system("tput setaf 7")
                os.system("clear")

            elif x==3:
              os.system("tput setaf 4")
              print("Enter the name of the VG to be created : ")
              os.system("tput setaf 7")
              vg_name = input()
              os.system("tput setaf 4")
              print("Enter the PVs(Separate by space if more than one) : ")
              os.system("tput setaf 7")
              pv_names = input()
              os.system("tput setaf 2")
              print("Creating Volume Group.....\n")
              os.system("tput setaf 7")
              if os.system("ssh %s vgcreate %s %s" %(remoteip, vg_name, pv_names))==0:
                os.system("tput setaf 3")
                print("Volume Group created")
                os.system("tput setaf 7")
                print()
                os.system("tput setaf 2")
                input("Press any key to continue")
                os.system("tput setaf 7")
              else:
                os.system("tput setaf 1")
                print("Cannot create Volume Group")
                os.system("tput setaf 2")
                print()
                input("Press any key to continue")
                os.system("tput setaf 7")
                os.system("clear")

            elif x==4:
              os.system("tput setaf 4")
              print("Enter the size of the partition : ")
              os.system("tput setaf 7")
              size = input()
              os.system("tput setaf 4")
              print("Enter the name of the LV to be created : ")
              os.system("tput setaf 7")
              lv_name = input()
              os.system("tput setaf 4")
              print("Enter the VG to be used: ")
              os.system("tput setaf 7")
              vg_name = input()
              os.system("tput setaf 3")
              print("Creating Logical Volume........")
              os.system("tput setaf 7")
              if os.system("ssh %s lvcreate --size +%sG --name %s %s" %(remoteip, size, lv_name, vg_name)) == 0:
                  os.system("tput setaf 3")
                  print("Logical Volume %s has been created" %lv_name)
                  os.system("tput setaf 2")
                  print()
                  input("Press any key to continue")
                  os.system("tput setaf 7")
              else:
                  os.system("tput setaf 1")
                  print("Cannot create LV")
                  os.system("tput setaf 2")
                  print()
                  input("Press any key to continue")
                  os.system("tput setaf 7")
              os.system("clear")

            elif x==5:
                os.system("tput setaf 4")
                print("Enter the name of the LV to be mounted: ")
                os.system("tput setaf 7")
                lv_name = input()
                os.system("tput setaf 4")
                print("Enter the directory location : ")
                os.system("tput setaf 7")
                dir_name = input()
                os.system("tput setaf 3")
                print("Formatting volume.....")
                os.system("tput setaf 7")
                if os.system("ssh %s mkfs.ext4 %s" %(remoteip, lv_name))==0:
                    os.system("tput setaf 3")
                    print("LV formatted\n")
                    os.system("tput setaf 3")
                    print("Mounting Volume.......")
                    os.system("tput setaf 7")
                    if os.system("ssh %s mount %s %s" %(remoteip, lv_name, dir_name)) == 0:
                      os.system("tput setaf 3")
                      print("LV has been mounted on %s (%s)" %(dir_name,remoteip))
                      os.system("tput setaf 2")
                      print()
                      input("Press any key to continue")
                      os.system("tput setaf 7")
                    else:
                      os.system("tput setaf 1")
                      print("Cannot mount volume. Please recheck the directory")
                      os.system("tput setaf 2")
                      print()
                      input("Press any key to continue")
                      os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot format the volume")
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                os.system("clear")
            
            elif x==6:
                os.system("tput setaf 4")
                print("Enter the VG name to be extended : ")
                os.system("tput setaf 7")
                vg_name = input()
                os.system("tput setaf 4")
                print("Enter the disk names to be appended(Separate by space if more than one) : ")
                os.system("tput setaf 7")
                disk_names = input()
                os.system("tput setaf 3")
                print("Extending the Volume Group......")
                os.system("tput setaf 7")
                if os.system("ssh %s vgextend %s %s" %(remoteip, vg_name, disk_names))==0:
                    os.system("tput setaf 3")
                    print("Volume Group %s extended" %vg_name)
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot extend VG")
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                os.system("clear")

            elif x==7:
                os.system("tput setaf 4")
                print("Enter the name of the LV to be extended : ")
                os.system("tput setaf 7")
                lv_name = input()
                os.system("tput setaf 4")
                print("Enter the size of extension : ")
                os.system("tput setaf 7")
                size = input()
                os.system("tput setaf 3")
                print("Extending the Logical Volume....")
                os.system("tput setaf 7")
                if os.system("ssh %s lvextend --size +%sG %s" %(remoteip, size, lv_name))==0:
                    os.system("tput setaf 3")
                    print("Resizing the partition......")
                    os.system("tput setaf 7")
                    if os.system("ssh %s resize2fs %s" %(remoteip, lv_name))==0:
                        os.system("tput setaf 3")
                        print("Logical Volume %s has been extended successfully" %lv_name)
                        os.system("tput setaf 2")
                        print()
                        input("Press any key to continue")
                        os.system("tput setaf 7")
                    else:
                        os.system("tput setaf 1")
                        print("Cannot resize the partition. Volume remains unextended")
                        os.system("tput setaf 2")
                        print()
                        input("Press any key to continue")
                        os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot extend the volume")
                    os.system("tput setaf 2")
                    print()
                    input("Press any key to continue")
                    os.system("tput setaf 7")
                os.system("clear")

            elif x==8:
                os.system("clear")
                
                while True:
                    os.system("tput setaf 1")
                    print("\t\t\t\t\t\t Display")
                    os.system("tput setaf 7")
                    print("\t\t\t\t\t--------------------------")
                    display()
                    os.system("tput setaf 3")
                    print("\n\t\t\tEnter your Choice : ",end=" ")
                    os.system("tput setaf 7")
                    d=int(input())

                    if d==1:
                        os.system("tput setaf 7")
                        display_all = input("Do you want to display the info of all PVs? (y/n) : ")
                        if display_all=="y":
                            os.system("tput setaf 3")
                            print("Displaying available Physical Volumes.....")
                            os.system("tput setaf 7")
                            os.system("ssh %s pvdisplay" %remoteip)
                            os.system("tput setaf 2")
                            print()
                            input("Press eny key to continue")
                            os.system("tput setaf 7")

                        else:
                            os.system("tput setaf 4")
                            print("Enter the name of the PV to be displayed : ")
                            os.system("tput setaf 7")
                            pv_name = input()
                            os.system("tput setaf 3")
                            print("Displaying Physical Volume %s......." %pv_name)
                            os.system("tput setaf 7")
                            os.system("ssh %s pvdisplay %s" %(remoteip,pv_name))
                            os.system("tput setaf 2")
                            print()
                            input("Press any key to continue")
                            os.system("tput setaf 7")
                        os.system("clear")
                            
                    elif d==2:
                        os.system("tput setaf 7")
                        display_all = input("Do you want to display the info of all VGs? (y/n) : ")
                        if display_all=="y":
                            os.system("tput setaf 3")
                            print("Displaying available Volume Groups.....")
                            os.system("tput setaf 7")
                            os.system("ssh %s vgdisplay" %remoteip)
                            os.system("tput setaf 2")
                            print()
                            input("Press eny key to continue")
                            os.system("tput setaf 7")
                        else:
                            os.system("tput setaf 4")
                            print("Enter the name of the VG to be displayed : ")
                            os.system("tput setaf 7")
                            vg_name = input()
                            os.system("tput setaf 3")
                            print("Displaying Volume Group %s......." %vg_name)
                            os.system("tput setaf 7")
                            os.system("ssh %s vgdisplay %s" %(remoteip, vg_name))
                            os.system("tput setaf 2")
                            print()
                            input("Press any key to continue")
                            os.system("tput setaf 7")
                        os.system("clear")

                    elif d==3:
                        os.system("tput setaf 7")
                        display_all = input("Do you want to display the info of all LVs? (y/n) : ")
                        if display_all=="y":
                            os.system("tput setaf 3")
                            print("Displaying available Logical Volumes.....")
                            os.system("tput setaf 7")
                            os.system("ssh %s lvdisplay" %remoteip)
                            os.system("tput setaf 2")
                            print()
                            input("Press eny key to continue")
                            os.system("tput setaf 7")
                        else:
                            os.system("tput setaf 4")
                            print("Enter the name of the LV to be displayed : ")
                            os.system("tput setaf 7")
                            lv_name = input()
                            os.system("tput setaf 3")
                            print("Displaying Logical Volume %s......." %lv_name)
                            os.system("tput setaf 7")
                            os.system("ssh %s lvdisplay %s" %(remoteip, lv_name))
                            os.system("tput setaf 2")
                            print()
                            input("Press any key to continue")
                            os.system("tput setaf 7")
                        os.system("clear")

                    elif d==4:
                        os.system("tput setaf 3")
                        print("Displaying the mounted directories......")
                        os.system("tput setaf 7")
                        os.system("ssh %s df -hT" %remoteip)
                        os.system("tput setaf 2")
                        print()
                        input("Press any key to continue")
                        os.system("tput setaf 7")
                        os.system("clear")

                    elif d==0:
                        os.system("clear")
                        break

                    else:
                      os.system("tput setaf 1")
                      print("=>Option not supported!")
                      os.system("tput setaf 2")
                      input("Press any key to continue")
                      os.system("clear")

            
            elif x==9:
                os.system("clear")
                break

            
            elif x==0:
                os.system("tput setaf 1")
                print("=>Exiting.....")
                os.system("tput setaf 7")
                os.system("sleep 1")
                os.system("clear")
                exit()

            else:
                os.system("tput setaf 1")
                print("=>Option not supported!")
                os.system("tput setaf 2")

                input("Press any key to continue")
                os.system("clear")
                os.system("tput setaf 1")
                print("\t\t\t\t\t\t LVM")
                os.system("tput setaf 7")
                print("\t\t\t\t\t--------------------------")

      
      elif y==2:
        while True:
          os.system("clear")
          os.system("tput setaf 1")
          print("\t\t\t\t\t\t Hadoop")
          os.system("tput setaf 7")
          print("\t\t\t\t\t--------------------------")

          hadoop_menu()
          os.system("tput setaf 3")
          print("\n\t\t\tEnter your Choice : ",end=" ")
          os.system("tput setaf 7")
          x=int(input())
          
          if location=="remote":
 
            if x==1:
              os.system("tput setaf 4")
              if os.system("ssh %s rpm -q jdk1.8" %remoteip ) == 0 and os.system("ssh %s rpm -q hadoop" %remoteip) == 0:
                  os.system("tput setaf 3")
                  print("Softwares installed already.....\nNow configuring.....")
                  os.system("tput setaf 7")
                  os.system("sleep 1")
                  node = input("What do you want the system(%s) to be configured as? (Namenode/Datanode) : " %remoteip)
                  y=2
                  os.system("tput setaf 4")
                  print("Configuring hdfs-site.xml.....")
                  os.system("tput setaf 7")
                  hadoop_hdfs_conf(node, "remote")
                  os.system("tput setaf 4")
                  print("Configuring core-site.xml.....")
                  os.system("tput setaf 7")
                  hadoop_core_conf(node, "remote")
                  os.system("tput setaf 2")
                  print("Hadoop %s configured successfully!" %node)
          
              elif os.system("ssh %s rpm -q jdk1.8" %remoteip ) != 0 or os.system("ssh %s rpm -q hadoop" %remoteip) != 0:
                os.system("tput setaf 7")
                loc = input("Mention the directory where the software files are downloaded : ")
                os.system("tput setaf 4")
                print("Installing Softwares.....")
                os.system("tput setaf 3")
                if os.system("ssh %s rpm -ivh %s/* --force" %(remoteip, loc)) == 0:
                  os.system("tput setaf 7")
                  print("Softwares installed successfully\n")
                  os.system("tput setaf 2")
                  node = input("What do you want the system(%s) to be configured as? (Namenode/Datanode) : " %remoteip)
                  y=2
                  os.system("tput setaf 4")
                  print("Configuring hdfs-site.xml.....")
                  os.system("tput setaf 7")
                  hadoop_hdfs_conf(node, "remote")
                  os.system("tput setaf 4")
                  print("Configuring core-site.xml.....")
                  os.system("tput setaf 7")
                  hadoop_core_conf(node, "remote")
                  os.system("tput setaf 2")
                  print("Hadoop %s configured successfully!" %node)

                else:
                  os.system("tput setaf 1")
                  print("Cannot install the softwares!\nConcluding....")
                         
              os.system("tput setaf 7")
              input("Press any key to continue")
              os.system("clear")
    
            elif x==2:
              os.system("tput setaf 3")
              print("Namenode/Datanode : ", end='')
              os.system("tput setaf 7")
              node = input()
              os.system("tput setaf 4")
              if node == "namenode" or node == "Namenode" or node == "NameNode" or node == "NAMENODE":   
                print("Formatting directory.....")
                os.system("tput setaf 7")
                if os.system("ssh %s hadoop namenode -format" %remoteip) == 0:
                  print("Directory formatted")
                  os.system("tput setaf 3")
                  print("Starting Namenode Services...")
                  os.system("tput setaf 7")
                  if os.system("ssh %s hadoop-daemon.sh start namenode" %remoteip) == 0:
                    os.system("tput setaf 2")
                    print("Hadoop Namenode Services started")
                  elif os.system("ssh %s hadoop-daemon.sh start namenode" %remoteip) == 256:
                    print()
                    os.system("tput setaf 7")
                    stop_process = input("Do you want to stop the currently active Namenode server? (y/n)")
                    if stop_process == "y":
                      os.system("tput setaf 3")
                      os.system("ssh %s hadoop-daemon.sh stop namenode" %remoteip)
                      os.system("tput setaf 7")
                      os.system("tput setaf 3")
                      print("Retarting Namenode Services...")
                      os.system("tput setaf 7")
                      if os.system("ssh %s hadoop-daemon.sh start namenode" %remoteip) == 0:
                        os.system("tput setaf 2")
                        print("Hadoop Namenode Services started")

                    elif stop_process == "n":
                      os.system("tput setaf 3")
                      print("Cannot start Namenode when one is running already!\nConcluding....")
                  
                  else:
                    os.system("tput setaf 1")
                    print("Cannot start the Namenode Services")
                    os.system("tput setaf 7")
                else:
                  os.system("tput setaf 1")
                  print("Cannot format directory. Please try again")
                  os.system("tput setaf 7")
              
              if node == "datanode" or node == "Datanode" or node == "DataNode" or node == "DATANODE":
                os.system("tput setaf 3")
                print("Starting Datanode Services...")
                os.system("tput setaf 7")
                if os.system("ssh %s hadoop-daemon.sh start datanode" %remoteip) == 0:
                  os.system("tput setaf 2")
                  print("Hadoop Datanode Services started")
                else:
                  os.system("tput setaf 1")
                  print("Cannot start the Datanode Services")
                  os.system("tput setaf 7")
        
              os.system("tput setaf 7")
              input("Press any key to continue")
              os.system("clear")
    
            elif x==3:
              os.system("tput setaf 7")
              master_ip = input("Enter the Namenode IP : ")
              os.system("tput setaf 4")
              print("Displaying the Cluster Report.....\n")
              os.system("tput setaf 7")
              if os.system("ssh %s hadoop dfsadmin -report" %master_ip) == 0:
                  input("\nPress any key to continue")
                  os.system("clear")
              else:
                  os.system("tput setaf 1")
                  print("Cannot display the report")
                  input("\nPress any key to continue")
                  os.system("tput setaf 7")
                  os.system("clear")
    
            elif x==4:
              master_ip = input("Enter the Namenode IP : ")
              os.system("tput setaf 4")
              print("Displaying the files uploaded....")
              os.system("tput setaf 7")
              os.system("ssh %s hadoop fs -ls /" %master_ip)
              os.system("tput setaf 2")
              input("\nPress any key to continue")
              os.system("tput setaf 7")
              os.system("clear")
    
            elif x==5:
              master_ip = input("Enter the Namenode IP : ")
              filefs = input("Enter the name of the uploaded file you want to read : ")
              os.system("tput setaf 4")
              print("Reading %s....." %filefs)
              os.system("tput setaf 7")
              os.system("ssh %s hadoop fs -cat /%s" %(master_ip, filefs))
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")
            

            elif x==6:
              slave_ip = input("Enter the Datanode IP : ")
              filefs = input("Enter the location of the file in %s you want to upload on the Cluster : " %slave_ip)
              os.system("tput setaf 4")
              print("Uploading.....")
              os.system("tput setaf 7")
              os.system("ssh %s hadoop fs -put %s /" %(slave_ip, filefs))
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")

            elif x==7:
              node = input("Namenode/Datanode : ")
              os.system("tput setaf 3")
              print("Enter the %s IP : " %node)
              os.system("tput setaf 7")
              node_ip = input()
              os.system("tput setaf 4")
              print("Stopping %s (%s)....." %(node, node_ip))
              os.system("tput setaf 7")
              if node=="namenode" or node=="Namenode" or node=="NameNode" or node=="NAMENODE":
                if os.system("ssh %s hadoop-daemon.sh stop namenode" %node_ip) == 0:
                    os.system("tput setaf 3")
                    print("Namenode stopped successfully")
                    os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot stop Namenode services!")
                    os.system("tput setaf 7")
              if node=="datanode" or node=="Datanode" or node=="DataNode" or node=="DATANODE":
                if os.system("ssh %s hadoop-daemon.sh stop datanode" %node_ip) == 0:
                    os.system("tput setaf 3")
                    print("Datanode stopped successfully")
                    os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot stop Datanode services!")
                    os.system("tput setaf 7")
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")

        
            elif x==9:
              os.system("clear")
              break
          
            elif x==0:
              os.system("tput setaf 1")
              print("=>Exiting.....")
              os.system("tput setaf 7")
              os.system("sleep 1")
              os.system("clear")
              exit()

            else:
              os.system("tput setaf 1")
              print("=>Option not supported!")
              os.system("tput setaf 7")
    
              input("Press any key to continue")
              os.system("clear")
              os.system("tput setaf 1")
              print("\t\t\t\t\t\t Welcome")
              os.system("tput setaf 7")
              print("\t\t\t\t\t--------------------------")
                
      
          elif location=="local":

            if x==1:
              os.system("tput setaf 4")
              if os.system("rpm -q jdk1.8") == 0 and os.system("rpm -q hadoop") == 0:
                os.system("tput setaf 3")
                print("Softwares installed already.....\nNow configuring.....")
                os.system("tput setaf 7")
                os.system("sleep 1")
                node = input("What do you want the system to be configured as? (Namenode/Datanode) : ")
                y=2
                os.system("tput setaf 4")
                print("Configuring hdfs-site.xml.....")
                os.system("tput setaf 7")
                hadoop_hdfs_conf(node, "local")
                os.system("tput setaf 4")
                print("Configuring core-site.xml.....")
                os.system("tput setaf 7")
                hadoop_core_conf(node, "local")
                os.system("tput setaf 2")
                print("Hadoop %s configured successfully!" %node)
          
              elif os.system("rpm -q jdk1.8") != 0 or os.system("rpm -q hadoop") != 0:
                os.system("tput setaf 7")
                loc = input("Mention the directory where the software files are downloaded : ")
                os.system("tput setaf 4")
                print("Installing Softwares.....")
                os.system("tput setaf 3")
                if os.system("rpm -ivh %s/* --force" %loc) == 0:
                  os.system("tput setaf 7")
                  print("Softwares installed successfully\n")
                  os.system("tput setaf 2")
                  node = input("What do you want the system to be configured as? (Namenode/Datanode) : ")
                  os.system("tput setaf 4")
                  print("Configuring hdfs-site.xml.....")
                  os.system("tput setaf 7")
                  hadoop_hdfs_conf(node, "local")
                  os.system("tput setaf 4")
                  print("Configuring core-site.xml.....")
                  os.system("tput setaf 7")
                  hadoop_core_conf(node, "local")
                  os.system("tput setaf 2")
                  print("Hadoop %s configured successfully!" %node)

                else:
                  os.system("tput setaf 1")
                  print("Cannot install the softwares!\nConcluding....")

          
              os.system("tput setaf 7")
              input("Press any key to continue")
              os.system("clear")
    
            elif x==2:
              os.system("tput setaf 3")
              print("Namenode/Datanode : ", end='')
              os.system("tput setaf 7")
              node = input()
              os.system("tput setaf 4")
              if node == "namenode" or node == "Namenode" or node == "NameNode" or node == "NAMENODE":   
                print("Formatting directory.....")
                os.system("tput setaf 7")
                if os.system("hadoop namenode -format") == 0:
                  print("Directory formatted")
                  os.system("tput setaf 3")
                  print("Starting Namenode Services...")
                  os.system("tput setaf 7")
                  if os.system("hadoop-daemon.sh start namenode") == 0:
                    os.system("tput setaf 2")
                    print("Hadoop Namenode Services started")
                  elif os.system("hadoop-daemon.sh start namenode") == 256:
                    print()
                    os.system("tput setaf 7")
                    stop_process = input("Do you want to stop the currently active Namenode server? (y/n)")
                    if stop_process == "y":
                      os.system("tput setaf 3")
                      os.system("hadoop-daemon.sh stop namenode")
                      os.system("tput setaf 7")
                      os.system("tput setaf 3")
                      print("Retarting Namenode Services...")
                      os.system("tput setaf 7")
                      if os.system("hadoop-daemon.sh start namenode") == 0:
                        os.system("tput setaf 2")
                        print("Hadoop Namenode Services started")

                    elif stop_process == "n":
                      os.system("tput setaf 3")
                      print("Cannot start Namenode when one is running already!\nConcluding....")
                  
                  else:
                    os.system("tput setaf 1")
                    print("Cannot start the Namenode Services")
                    os.system("tput setaf 7")
                else:
                  os.system("tput setaf 1")
                  print("Cannot format directory. Please try again")
                  os.system("tput setaf 7")
              
              if node == "datanode" or node == "Datanode" or node == "DataNode" or node == "DATANODE":
                os.system("tput setaf 3")
                print("Starting Datanode Services...")
                os.system("tput setaf 7")
                if os.system("hadoop-daemon.sh start datanode") == 0:
                  os.system("tput setaf 2")
                  print("Hadoop Datanode Services started")
                else:
                  os.system("tput setaf 1")
                  print("Cannot start the Datanode Services")
                  os.system("tput setaf 7")
        
              os.system("tput setaf 7")
              input("Press any key to continue")
              os.system("clear")
    
            elif x==3:
              os.system("tput setaf 7")
              master_ip = input("Enter the Namenode IP : ")
              os.system("tput setaf 4")
              print("Displaying the Cluster Report.....\n")
              os.system("tput setaf 7")
              if os.system("ssh %s hadoop dfsadmin -report" %master_ip) == 0:
                input("\nPress any key to continue")
                os.system("clear")
              else:
                os.system("tput setaf 1")
                print("Cannot display the report")
                input("\nPress any key to continue")
                os.system("tput setaf 7")
                os.system("clear")
    
            elif x==4:
              master_ip = input("Enter the Namenode IP : ")
              os.system("tput setaf 4")
              print("Displaying the files uploaded....")
              os.system("tput setaf 7")
              os.system("ssh %s hadoop fs -ls /" %master_ip)
              os.system("tput setaf 2")
              input("\nPress any key to continue")
              os.system("tput setaf 7")
              os.system("clear")
    
            elif x==5:
              master_ip = input("Enter the Namenode IP : ")
              filefs = input("Enter the name of the uploaded file you want to read : ")
              os.system("tput setaf 4")
              print("Reading %s....." %filefs)
              os.system("tput setaf 7")
              os.system("ssh %s hadoop fs -cat /%s" %(master_ip, filefs))
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")
            

            elif x==6:
              slave_ip = input("Enter the Datanode IP : ")
              filefs = input("Enter the location of the file in %s you want to upload on the Cluster : " %slave_ip)
              os.system("tput setaf 4")
              print("Uploading.....")
              os.system("tput setaf 7")
              os.system("ssh %s hadoop fs -put %s /" %(slave_ip, filefs))
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")

            elif x==7:
              node = input("Namenode/Datanode : ")
              os.system("tput setaf 3")
              print("Enter the %s IP : " %node)
              os.system("tput setaf 7")
              node_ip = input()
              os.system("tput setaf 4")
              print("Stopping %s (%s)....." %(node, node_ip))
              os.system("tput setaf 7")
              if node=="namenode" or node=="Namenode" or node=="NameNode" or node=="NAMENODE":
                if os.system("ssh %s hadoop-daemon.sh stop namenode" %node_ip) == 0:
                    os.system("tput setaf 3")
                    print("Namenode stopped successfully")
                    os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot stop Namenode services!")
                    os.system("tput setaf 7")
              if node=="datanode" or node=="Datanode" or node=="DataNode" or node=="DATANODE":
                if os.system("ssh %s hadoop-daemon.sh stop datanode" %node_ip) == 0:
                    os.system("tput setaf 3")
                    print("Datanode stopped successfully")
                    os.system("tput setaf 7")
                else:
                    os.system("tput setaf 1")
                    print("Cannot stop Datanode services!")
                    os.system("tput setaf 7")
              os.system("tput setaf 2")
              input("Press any key to continue")
              os.system("tput setaf 7")
              os.system("clear")
            
            elif x==9:
              os.system("clear")
              break

        
            elif x==0:
              os.system("tput setaf 1")
              print("=>Exiting.....")
              os.system("tput setaf 7")
              os.system("sleep 1")
              os.system("clear")
              exit()

            else:
              os.system("tput setaf 1")
              print("=>Option not supported!")
              os.system("tput setaf 7")
    
              input("Press any key to continue")
              os.system("clear")
              os.system("tput setaf 1")
              print("\t\t\t\t\t\t Welcome")
              os.system("tput setaf 7")
              print("\t\t\t\t\t--------------------------")
                     
      elif y==1:
          while True:
            os.system("clear")
            os.system("tput setaf 1")
            print("\t\t\t\t\t\t AWS")
            os.system("tput setaf 7")
            print("\t\t\t\t\t--------------------------")

            aws_menu()
            os.system("tput setaf 3")
            print("\n\t\t\tEnter your Choice : ",end=" ")
            os.system("tput setaf 7")
            x=int(input())

            if location=="local":
                if x==9:
                    os.system("clear")
                    break

                elif x==0:
                    os.system("tput setaf 1")
                    print("=>Exiting.....")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()
                
                else:
                    aws_functions("local", x)

            elif location=="remote":
                if x==9:
                    os.system("clear")
                    break

                elif x==0:
                    os.system("tput setaf 1")
                    print("=>Exiting.....")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()

                else:
                    aws_functions("remote", x, remoteip)

            
      elif y==3:
          while True:
            os.system("clear")
            os.system("tput setaf 1")
            print("\t\t\t\t\t\t Docker")
            os.system("tput setaf 7")
            print("\t\t\t\t\t--------------------------")

            docker_menu()
            os.system("tput setaf 3")
            print("\n\t\t\tEnter your Choice : ",end=" ")
            os.system("tput setaf 7")
            x=int(input())

            if location=="local":
                if x==9:
                    os.system("clear")
                    break

                elif x==0:
                    os.system("tput setaf 1")
                    print("=>Exiting.....")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()

                else:
                    docker_functions("local", x)

            if location=="remote":
                if x==9:
                    os.system("clear")
                    break

                elif x==0:
                    os.system("tput setaf 1")
                    print("=>Exiting.....")
                    os.system("tput setaf 7")
                    os.system("sleep 1")
                    os.system("clear")
                    exit()

                else:
                    docker_functions("remote", x, remoteip)


      
      elif y==0:
        os.system("tput setaf 1")
        print("=>Exiting.....")
        os.system("tput setaf 7")
        os.system("sleep 1")
        os.system("clear")
        exit()

      else:
        os.system("tput setaf 1")
        print("=> Option Not Supported!")
        os.system("tput setaf 7")
        input("Press any key to continue")
        os.system("clear")



