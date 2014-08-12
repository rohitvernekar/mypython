from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url='http://buildout.zeomega.org/jenkins/'
    server=Jenkins(jenkins_url,username="grohit",password="jenkins")
    return server


def disable_job():
    server=get_server_instance()
    view='BCBSFL'
    if view in server.views.keys():
        job_name='test'
        if (server.has_job(job_name)):
            job_instance=server.get_job(job_name)
            #print dir(job_instance)
            print 'Job Name:%s' %(job_instance.name)
            print 'Job Description:%s' % (job_instance.get_description())
            print 'Is Job running :%s' %(job_instance.is_running())
            print 'Is Job enabled:%s' % (job_instance.is_enabled())
            if job_instance.is_enabled():
                job_instance.disable()
            else:
                pass
            print "%s is already disabled" % job_instance.name
            print 'Is Job running :%s' %(job_instance.is_running())
            print 'Is Job enabled:%s' % (job_instance.is_enabled())
         
if __name__=='__main__':
    disable_job()
     
