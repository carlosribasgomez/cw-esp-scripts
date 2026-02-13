"""
Aplica reglas de ortografia a todos los archivos del proyecto:
1. Elimina signos de apertura: ¿ → (nada), ¡ → (nada)
2. Elimina tildes: á→a, é→e, í→i, ó→o, ú→u, Á→A, É→E, Í→I, Ó→O, Ú→U
Mantiene: ñ, Ñ (son letras, no acentos)
"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

REPLACEMENTS = {
    '¿': '',
    '¡': '',
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ú': 'U',
}

def fix_text(text):
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    fixed = fix_text(original)
    if fixed != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        count = sum(original.count(old) for old in REPLACEMENTS if REPLACEMENTS[old] != old or old in ('¿', '¡'))
        print(f"  [OK] {os.path.basename(path)} — {count} cambios")
        return True
    else:
        print(f"  [--] {os.path.basename(path)} — sin cambios")
        return False

def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    targets = [
        # Model configs
        os.path.join(base, 'tools', 'models', 'ailen_free.py'),
        os.path.join(base, 'tools', 'models', 'dari_urdaneta.py'),
        # Dari manual HTML pages
        os.path.join(base, 'dari-urdaneta', 'training.html'),
        os.path.join(base, 'dari-urdaneta', 'broadcasts.html'),
        os.path.join(base, 'dari-urdaneta', 'phrases.html'),
        # PDF generator
        os.path.join(base, 'tools', 'generate_client_pdf.py'),
        # Model factory (UI labels)
        os.path.join(base, 'tools', 'model_factory.py'),
        # Main dashboard
        os.path.join(base, 'index.html'),
    ]
    
    print("=== CORRIGIENDO ORTOGRAFIA ===\n")
    changed = 0
    for path in targets:
        if os.path.exists(path):
            if process_file(path):
                changed += 1
        else:
            print(f"  [!!] No encontrado: {path}")
    
    print(f"\n[DONE] {changed} archivos modificados")

if __name__ == '__main__':
    main()
