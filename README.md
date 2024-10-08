# Project Starter
This repository contains the starter code for the **Ensuring Quality Releases** project of the cd1807 Ensuring Quality Releases (Quality Assurance) course taught by Nathan Anderson. 


## How to use?
- Fork this repository to your Github account and clone it locally for further development. 
- Follow the classroom instructions, and check the rubric before a submission. 

## Suggestions and Corrections
Feel free to submit PRs to this repo should you have any proposed changes. 

### Guideline
- Git clone {repository-url}
- Create vm-build Linux by Portal
- Create Storage Account for Terraform State with path bash `/terraform/environments/test/configure-tfstate-storage-account.sh
- Create Azure Devops PAT and ARM Service Connection with Storage Account Contributor Role
- Install Azure Devops agent build
- Capture image from vm-build
- Create Azure Devops Environment & Resources
- Create Azure Devops Pipeline
- Install Terraform Extension from Marketplace
- Install dependences: python, npm, newman, chrome driver, chrome browser, java jdk, jmeter,...
- Execute Pipeline successfully
- Configure Action Group & Alert
- Configure Log from vm & query by KQL
### Structure
1. `automatedtesting` folder contains automated testing methods
    - `jmeter` folder contains performance test suites and application source code
    - `postman` folder contains validation and regression test suites 
    - `selenium` folder contains ui test suites 
2. `screenshots` folder contains all screenshots when implements tasks
3. `terraform` folder contains all infrastructure as code
4. `azure-pipelines.yaml` contains all code stage code CI/CD of project

