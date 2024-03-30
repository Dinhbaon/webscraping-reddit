package WebScrapingCollegeResults;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@EnableJpaRepositories
@EnableAspectJAutoProxy(proxyTargetClass = true)
@EnableTransactionManagement
@SpringBootApplication
public class WebScrapingCollegeResultsApplication {

	public static void main(String[] args) {
		SpringApplication.run(WebScrapingCollegeResultsApplication.class, args);
	}

}
