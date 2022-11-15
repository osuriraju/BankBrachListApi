# API for getting Bank Details for required Branch

We can simply get the bank details for given branch name.

# Development and Method Used

This project is developed using Django Framework.
I have used rest_framework module to get the details in a json template.
I have used rest_framework viewsets as ReadOnlyModelViewSet, because we are not changing the details of the bank but we are accessing the details. So I used ReadOnlyModelViewSet.
Whenever the user enters the branch name in the url, the views.py gets the query params and filters the whole data of banks with the branch name.
And shows the filtered data with given branch name.


It took 3 days for me to complete.

# Usage

Simply open the project in django environment, and search the branch name in the URL.


```
EX : In the URL type, 'MainURL/branch', and press enter to get the details of the branch.

Note : Branch name should be correct, no need to worry about case sensitive.
```

