'''
Defines a class, Neuron472442377, of neurons from Allen Brain Institute's model 472442377

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472442377:
    def __init__(self, name="Neuron472442377", x=0, y=0, z=0):
        '''Instantiate Neuron472442377.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472442377_instance is used instead
        '''
        
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Nr5a1-Cre_Ai14_IVSCC_-177332.03.01.01_475407854_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472442377_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 109.05
            sec.e_pas = -93.3055648804
        for sec in self.apic:
            sec.cm = 1.98
            sec.g_pas = 0.000290848207298
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000273327365018
        for sec in self.dend:
            sec.cm = 1.98
            sec.g_pas = 2.37936671547e-06
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.00115635
            sec.gbar_Ih = 0
            sec.gbar_NaTs = 0.76478
            sec.gbar_Nap = 7.723e-05
            sec.gbar_K_P = 0.0078138
            sec.gbar_K_T = 3.6467e-05
            sec.gbar_SK = 0.000450277
            sec.gbar_Kv3_1 = 0.0781963
            sec.gbar_Ca_HVA = 1.29574e-05
            sec.gbar_Ca_LVA = 0.006362
            sec.gamma_CaDynamics = 0.00528637
            sec.decay_CaDynamics = 831.652
            sec.g_pas = 0.000161294
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

