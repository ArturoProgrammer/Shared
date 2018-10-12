import SFSProjectCommand as SFSPC


def writeTemplate (templatefile, option):
	"""Funcion para escribir el archivo .xml sobre el proyecto"""
	
	template = open(templatefile, 'r')
	templatefile.read()

	if option == "Manifest":
		"""Escribe el contenido del archivo Manifest.xml"""
		writeTemplate = open("Manifest.xml", 'w')
		writeTemplate.write("""
<application name="{app_name}"
	version="{app_version}"
	licenses="{app_licenses}">

	<software>
		<sys use:software="{soft_shared}"> <!--Git, SFS, etc.-->
		
		<app code="{app_code}">
		<app author="{app_author}">
	</software>
</application>
""".format(app_name = aname, app_versionv = aversion, app_licenses = alicenses, soft_shared = sshared, app_code = acode, app_author = aauthor))
	elif option == "SharedSystem":
		pass
	elif option == "CopyProject":
		"""Realiza una copia del proyecto"""
		pass
	else:
		print "ERROR"

def onStart ():
	# Funcion a ejecutar cuando se inicie la aplicaicon
	SFSPC.NewProject()

if __name__ == '__main__':
	onStart()