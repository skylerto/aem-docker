FROM inlet/aem-base
MAINTAINER Adfinis SyGroup/Namics

# Extracts AEM
WORKDIR /aem
# RUN java -XX:MaxPermSize=256m -Xmx1024M -jar AEM_6.3_Quickstart.jar -unpack -r publish -p 4503

# Add customised log file, to print the logging to standard out.
COPY org.apache.sling.commons.log.LogManager.config /aem/crx-quickstart/install
COPY files/license.properties /aem/license.properties
COPY files/AEM_6.3_Quickstart.jar /aem/AEM_6.3_Quickstart.jar

# Installs AEM
# RUN python aemInstaller.py -i AEM_6.3_Quickstart.jar -r publish -p 4503
RUN ["python","aemInstaller.py","-i","AEM_6.3_Quickstart.jar","-r","publish","-p","4503"]
# RUN ["rm","-rf","AEM_6.3_Quickstart.jar"]

WORKDIR /aem/crx-quickstart/bin
#Replaces the port within the quickstart file with the standard publisher port
RUN sed -i "s|4502|4503|g" quickstart


EXPOSE 4503 8000
ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]
