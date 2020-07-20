Auto Ticket Assignment Application built as part of Capstone Project using NLP

<b> Project Overview</b>:

One of the key activities of any IT function is to “Keep the lights on” to ensure there is no
impact to the Business operations. IT leverages the Incident Management process to achieve the
above Objective. An incident is something that is an unplanned interruption to an IT service or
reduction in the quality of an IT service that affects the Users and the Business. The main goal of the
Incident Management process is to provide a quick fix / workarounds or solutions that resolves the
interruption and restores the service to its full capacity to ensure no business impact. In most of the
organizations, incidents are created by various Business and IT Users, End Users/ Vendors if they
have access to ticketing systems, and from the integrated monitoring systems and tools. Assigning
the incidents to the appropriate person or unit in the support team has critical importance to provide
improved user satisfaction while ensuring better allocation of support resources.
In the support process, incoming incidents are analyzed and assessed by organization’s
support teams to fulfill the request. In many organizations, better allocation and effective usage of
the valuable support resources will directly result in substantial cost savings.
In this capstone project, using a powerful AI / ML technique we will build a classifier that can
by analysing text in the incidents and classify incidents to right functional groups can help
organizations to reduce the resolving time of the issue and can focus on more productive tasks.

<b>Problem Statement</b>:
In most of the IT organizations, the assignment of incidents to appropriate IT groups is still a
manual process. Manual assignment of incidents is time consuming and requires human efforts.
There may be mistakes due to human errors and resource consumption is carried out ineffectively
because of the misaddressing. On the other hand, manual assignment increases the response and
resolution times which result in user satisfaction deterioration / poor customer service.


<b>Solution </b>:
This capstone project intends to reduce the manual intervention of IT operations or Service
desk teams by automating the ticket assignment process .
The goal here is to create a text classification based ML model that can automatically
classify any new tickets by analysing ticket description to one of the relevant Assignment groups,
which could be later integrated to any ITSM tool like Service Now
Based on the ticket description our model will output the probability of assigning it to one of the 74
Groups.

A flask application was built to deploy the models onto a web application
