# STEG 1: Enklaste möjliga logging
import logging

# Sätt upp grundläggande logging (gör detta en gång i början)
logging.basicConfig(
    level=logging.INFO,  # Visa INFO och högre (INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Hur meddelanden ser ut
)

# Skapa en logger för denna fil
logger = logging.getLogger(__name__)  # __name__ blir filnamnet

def exempel_1_enkelt():
    """Enklaste exemplet"""
    logger.info("Hej! Programmet startade")
    logger.info("Gör något...")
    logger.warning("Något konstigt hände, men det är okej")
    logger.error("Ett fel inträffade!")
    logger.info("Programmet slutar")

# STEG 2: Varför använder vi __name__?
# Testa båda och se skillnaden:

logger_med_namn = logging.getLogger(__name__)  # Visar filnamnet
logger_utan_namn = logging.getLogger("MinApp") # Visar "MinApp"

def exempel_2_namn():
    """Visa skillnaden mellan olika logger-namn"""
    logger_med_namn.info("Detta kommer från __name__")     # Visar: main - INFO - ...
    logger_utan_namn.info("Detta kommer från 'MinApp'")   # Visar: MinApp - INFO - ...

# STEG 3: Olika log-nivåer i praktiken
def exempel_3_niva():
    """Visa alla log-nivåer"""
    logger.debug("DEBUG: Detaljerad info (syns bara om level=DEBUG)")
    logger.info("INFO: Allmän information")
    logger.warning("WARNING: Något att hålla koll på")  
    logger.error("ERROR: Ett fel inträffade")
    logger.critical("CRITICAL: Allvarligt systemfel!")

# STEG 4: Logging med variabler
def exempel_4_variabler():
    """Hur man loggar variabler"""
    username = "Anna"
    age = 25
    items = ["äpple", "banan", "citron"]
    
    # Gamla sättet (fungerar men inte bäst)
    logger.info("Användaren " + username + " är " + str(age) + " år gammal")
    
    # Bättre sätt med f-strings
    logger.info(f"Användaren {username} är {age} år gammal")
    
    # Logga listor och komplexa objekt
    logger.info(f"Användaren har {len(items)} items: {items}")

# STEG 5: Hantera fel med logging
def exempel_5_felhantering():
    """Hur man loggar fel"""
    try:
        resultat = 10 / 0  # Detta kommer krascha
    except ZeroDivisionError as e:
        # Logga felet MED stack trace (exc_info=True)
        logger.error(f"Division med noll inträffade: {e}", exc_info=True)
        # exc_info=True visar EXAKT var felet hände
    
    try:
        nummer = int("inte_ett_nummer")
    except ValueError as e:
        # Ibland vill man inte ha hela stack trace
        logger.warning(f"Kunde inte konvertera till nummer: {e}")

# STEG 6: Conditional logging (smart!)
def exempel_6_villkorlig():
    """Bara logga ibland"""
    for i in range(100):
        # Logga bara varje 10:e iteration
        if i % 10 == 0:
            logger.info(f"Bearbetat {i} items...")
    
    # Eller använd olika nivåer beroende på situation
    error_count = 5
    if error_count > 0:
        logger.warning(f"Hittade {error_count} fel")
    else:
        logger.info("Inga fel hittades!")

# HUVUDFUNKTION - kör allt
def main():
    """Kör alla exempel"""
    print("=== EXEMPEL 1: ENKELT ===")
    exempel_1_enkelt()
    
    print("\n=== EXEMPEL 2: NAMN ===")
    exempel_2_namn()
    
    print("\n=== EXEMPEL 3: NIVÅER ===")
    exempel_3_niva()
    
    print("\n=== EXEMPEL 4: VARIABLER ===")
    exempel_4_variabler()
    
    print("\n=== EXEMPEL 5: FELHANTERING ===")
    exempel_5_felhantering()
    
    print("\n=== EXEMPEL 6: VILLKORLIG ===")
    exempel_6_villkorlig()

if __name__ == "__main__":
    main()


# BONUS: Ändra log-nivå för att se olika mängder output
def testa_olika_niva():
    """
    Testa att ändra level= i basicConfig ovan:
    
    level=logging.DEBUG   # Visar ALLT (debug, info, warning, error, critical)
    level=logging.INFO    # Visar info, warning, error, critical
    level=logging.WARNING # Visar bara warning, error, critical  
    level=logging.ERROR   # Visar bara error, critical
    """
    logger.debug("Detta syns bara om level=DEBUG")
    logger.info("Detta syns om level=INFO eller lägre")  
    logger.warning("Detta syns om level=WARNING eller lägre")
    logger.error("Detta syns nästan alltid")
    logger.critical("Detta syns alltid")

# Kör detta för att testa:
# testa_olika_niva()