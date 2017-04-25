package fr.botai.rafkaf.task;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import fr.botai.rafkaf.api.TradeCall;

@Component
public class TradeBatch {

	private Logger logger = LoggerFactory.getLogger(this.getClass());
	
	private TradeCall call;

	public TradeBatch(){
		this.call = new TradeCall();
	}
	
	@Scheduled(cron="0 */5 10-22 * * MON-FRI")
	public void cronJob(){
		logger.info("Chaque 5 min je vais lancer des appels pour avoir de nouvelles valeurs et lancer le script donnant la stratégie à adopter");
		System.out.println(call.callApiSpecific());
	}
	
	@Scheduled(cron="0 */2 10-22 * * MON-FRI")
	public void watchForDecision(){
		logger.info("Chaque jour toutes les deux minutes je guette une réponse et lance un appel pour l'éxécuter si nécessaire");
	}
	
	@Scheduled(cron="0 30 9 * * MON-FRI")
	public void cleanForNewDay(){
		logger.info("Chaque jour à 9h30 je lance un script de nettoyage de fichier et vide les données inutiles de la base");
	}

}
