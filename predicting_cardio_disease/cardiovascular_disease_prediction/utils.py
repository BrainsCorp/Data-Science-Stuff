import os

def savefig(obj, figname):
    '''
        obj: matplotlib object
    '''
    try:
        path_savefig = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), 'reports/figures/')
        obj.savefig(path_savefig + figname, dpi=300, format='png')
    except Exception as e:
        print(f"Error Occurred while Saving Figure {e}")
