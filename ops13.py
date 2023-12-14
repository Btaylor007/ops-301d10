# Define user information
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$samaccountname = "$firstName.$lastName"
$email = "ferdi@GlobeXpower.com"
$department = "TPS Department"
$location = "Springfield, OR"
$office = "GlobeX USA"
$title = "TPS Reporting Lead"

# Create the user object
$newUser = New-ADUser -Name $samaccountname -GivenName $firstName -Surname $lastName -DisplayName $displayName -EmailAddress $email -PasswordNotRequired -Department $department -Office $office -Title $title -Location $location

# Set the user's container (optional, adjust based on your AD structure)
$newUser.SetPath("OU=Employees,DC=GlobeX,DC=com")

# Update the user object
$newUser.Update()

# Write confirmation message
Write-Host "User '$displayName' created successfully!"

# Verify user creation in ADAC (optional)
Get-ADUser -Identity $samaccountname | Select-Object Name, GivenName, Surname, Department, Office, Title, Location

# Optionally, delete the user if needed
# Remove-ADUser -Identity $samaccountname
