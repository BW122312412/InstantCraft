# Instant Minecraft
Host on a powerful AWS server and save on server costs.

Minecraft server without this   : $80 / Month

Minecraft server with this      : $0.10 per hour while online and free while offline

Using AWS Instances and Python to seamlessly host an on demand minecraft server. This project uses a free EC2 server while no one is online and seamlessly switches to a higher tier EC2 server that the server will be hosted on while users are online. Includes an automatic shutdown when no one is online.

# Instructions
*Requires familiarity with command line*
*Requires knowing how to set up a minecraft server (I'd recommend practicing locally with a minecraft server first)*

## Setup

Create a **AWS account** and enter the **EC2 Dashboard**.

In the sidebar, under **Network & Security**, access **Security Groups**.

Select **Create security group**.

Add a **Security group name** and a **Description** and add two **inbound rules**:

|Type | Port range | Source|
|-|-|-|
|SSH | 22 | Anywhere|
|Custom TCP | 25565 | Anywhere|

In the sidebar, under **Network & Security**, access **Elastic IPs**.

Select **Allocate Elastic IP address** and **Allocate** it.

## Create Minecraft Server

In the sidebar, under **Instances**, access **Instances**.

Select **Launch instances**.
1. Choose an **Amazon Machine Image** (AMI) : Select **Amazon Linux 2**
2. Choose an **Instance Type**: Choose based on the server specs wanted. (I choose m4.xlarge)
3. Configure Instance Details: Leave as Default
4. Add **Storage**: Increase root to as much as you need (I choose 30), turn off Delete on termination and choose, and encryption.
5. Add Tags: Optional
6. Configure **Security Group**: Assign a security group to an **existing security group** and select the security group made earlier
7. Review: **Review and Launch**

Now **connect** to the new instance. You can use **EC2 Instance Connect**. (In case of error, validate your Security group)



In the command prompt setup your minecraft server.

    wget https://raw.githubusercontent.com/BW122312412/InstantCraft/master/init.sh
    chmod +x 
    sudo ./init.sh
    ./start.sh
    

## Create Proxy Server
In the sidebar, under **Instances**, access **Instances**.

Select **Launch instances**.
1. Choose an **Amazon Machine Image** (AMI) : Select **Amazon Linux 2 AMI**
2. Choose an **Instance Type**: Choose the free tier
3. Configure Instance Details: Leave as Default
4. Add Storage: Leave as Default
5. Add Tags: Optional
6. Configure **Security Group**: Assign a security group to an **existing security group** and select the security group made earlier
7. Review: **Review and Launch**

In the sidebar, under **Network & Security**, access **Elastic IPs**.

Select your **Previous Elastic IP** and **Associate** it with your proxy server.

Open a new tab with AWS. Search **Users** and under features open **Users**.

**Add user**. Add a name and grant **Programmatic access**.

In **Permissions** add **StartInstances**, **StopInstances**, **AssociateAddress**

Copy the **Access Key Id** and the **Secret Access Key**. (Temporarily store for next step)

Open the instance in a shell and enter:
    
    aws configure

Enter **Access Key Id** and **Secret Access Key** when prompted

Next run

    sudo yum install git
    git clone https://github.com/BW122312412/InstantCraft.git
    cd InstantCraft
    nano configure.py

Fill out the **configure.py**, then

    python instantMinecraft.py & 
    disown  -h  %1