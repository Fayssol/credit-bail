CREATE OR REPLACE FUNCTION update_montant_total_paye()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE askia_admin_versement
    SET montant_total_paye = (
        SELECT COALESCE(SUM(montant_versement), 0) 
        FROM askia_admin_versement 
        WHERE contrat_id = NEW.contrat_id
    )
    WHERE contrat_id = NEW.contrat_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_insert_update_montant_total_paye
AFTER INSERT ON askia_admin_versement
FOR EACH ROW
EXECUTE FUNCTION update_montant_total_paye();
