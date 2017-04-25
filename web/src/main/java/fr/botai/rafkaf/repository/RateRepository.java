package fr.botai.rafkaf.repository;

import javax.transaction.Transactional;

import org.springframework.data.repository.CrudRepository;

import fr.botai.rafkaf.model.Rate;

@Transactional
public interface RateRepository extends CrudRepository<Rate,Long> {

	
}
