$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'


# Install the venv
if (-not(Test-Path -Path "./.venv/")) {
	python -m venv .venv
	
}
else {
	Write-Host "venv already created"
}

# Activate the venv
.venv/scripts/activate

# Clone dependancy - anet-client - if and install into venv needed
if (-not (Test-Path -Path "./anet_client/" )) {
	git clone https://github.com/etomboulian/anet_client.git
	pushd anet_client
	pip install -r requirements.txt
	popd
}
else {
	Write-Host "anet client already installed"
}

# Install this applications requirements into venv
pip install -r requirements.txt

if (-not (Test-Path -Path ".env")) {
	New-Item .env
	"ORG_NAME=ljsupport12" >> .env
	"API_KEY=api_key_value" >> .env
	"API_SECRET=shared_secret_value" >> .env
	"COUNTRY=USA" >> .env
}


