FROM skylerto/aem-base
MAINTAINER Adfinis SyGroup/Namics

#Copies required build media
COPY postInstallHook.py /aem/postInstallHook.py
COPY files/license.properties /aem/license.properties
COPY files/AEM_6.3_Quickstart.jar /aem/AEM_6.3_Quickstart.jar

WORKDIR /aem

# Add customised log file, to print the logging to standard out.
COPY org.apache.sling.commons.log.LogManager.config /aem/crx-quickstart/install/

# Installs AEM
RUN ["python","aemInstaller.py","-i","AEM_6.3_Quickstart.jar","-r","author","-p","4502"]
# RUN ["rm","-rf","/aem/AEM_6.3_Quickstart.jar"]

EXPOSE 4502 8000
ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]
