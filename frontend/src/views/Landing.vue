<template>
  <div class="relative flex h-auto min-h-screen w-full flex-col group/design-root overflow-x-hidden">
    <div class="layout-container flex h-full grow flex-col">
      <!-- TopNavBar -->
      <header class="sticky top-0 z-50 bg-background-light/80 dark:bg-background-dark/80 backdrop-blur-sm">
        <div class="flex items-center justify-between whitespace-nowrap border-b border-solid border-gray-200 dark:border-gray-700 px-4 sm:px-10 py-3 max-w-7xl mx-auto">
          <div class="flex items-center gap-4 text-text-light dark:text-text-dark">
            <span class="material-symbols-outlined text-3xl text-primary">directions_car</span>
            <h2 class="text-lg font-bold leading-tight tracking-[-0.015em]">AutoExpert</h2>
          </div>
          <div class="hidden md:flex flex-1 justify-center items-center gap-9">
            <a class="text-text-light dark:text-text-dark text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary transition-colors" href="#services">Serviços</a>
            <a class="text-text-light dark:text-text-dark text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary transition-colors" href="#about">Sobre Nós</a>
            <a class="text-text-light dark:text-text-dark text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary transition-colors" href="#contact">Contato</a>
          </div>
          <div class="flex items-center gap-3">
            <router-link class="text-text-light dark:text-text-dark text-sm font-medium leading-normal hover:text-primary dark:hover:text-primary transition-colors" to="/login">Entrar</router-link>
            <a class="flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 px-4 bg-primary text-white text-sm font-bold leading-normal tracking-[0.015em] hover:opacity-90 transition-opacity" href="#contact">
              <span class="truncate">Agende Agora</span>
            </a>
          </div>
        </div>
      </header>
      <main class="flex-1">
        <!-- HeroSection -->
        <section class="py-10 sm:py-20">
          <div class="max-w-7xl mx-auto px-4 sm:px-10">
            <div class="@container">
              <div class="flex flex-col gap-8 @[864px]:flex-row-reverse items-center">
                <div class="w-full @[864px]:w-1/2">
                  <img class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-xl object-cover" data-alt="Modern auto repair shop with a car on a lift" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDDFN_o3Glr15DQHht2SzlYdRzpJE05nGCuWSx-bA1tgPux396O464KLrItDDnc8Ivp1i3MZRySjFU-tlyb6Le4MpNuVfu9yEBnXIbYqNBd9S1cfgzL2ii_L-fQpuq-s9vo5NfbXCHERtYS5XE2Frufd6IKpIrVoWOpvq8Y8DUxcvsEjFc__8xBN1HX6qCmH1RbgOTIppNnhdOrrznutDv-LwFPoNhBiRf3H6_zOiHIMo-FqoyK0UBdGsmMOc-1VscAfmaveuoubjR6"/>
                </div>
                <div class="flex flex-col gap-6 @[480px]:gap-8 @[864px]:w-1/2 @[864px]:justify-center">
                  <div class="flex flex-col gap-4 text-left">
                    <h1 class="text-text-light dark:text-text-dark text-4xl font-black leading-tight tracking-[-0.033em] @[480px]:text-5xl">
                      Cuidado Confiável e Moderno para o Seu Veículo
                    </h1>
                    <h2 class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal @[480px]:text-lg">
                      Utilizamos tecnologia de ponta e técnicos certificados para garantir o melhor serviço para o seu carro.
                    </h2>
                  </div>
                  <a class="flex w-full sm:w-auto max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-5 bg-primary text-white text-base font-bold leading-normal tracking-[0.015em] hover:opacity-90 transition-opacity" href="#contact">
                    <span class="truncate">Agende Seu Serviço Online</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- FeatureSection -->
        <section class="py-10 sm:py-20 bg-background-light dark:bg-background-dark border-t border-b border-gray-200 dark:border-gray-800" id="services">
          <div class="max-w-7xl mx-auto px-4 sm:px-10">
            <div class="flex flex-col gap-10 @container">
              <div class="flex flex-col gap-4 max-w-3xl">
                <h2 class="text-text-light dark:text-text-dark tracking-light text-[32px] font-bold leading-tight @[480px]:text-4xl @[480px]:font-black">Nossos Principais Serviços</h2>
                <p class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal">Oferecemos uma gama completa de serviços para manter seu veículo em perfeitas condições.</p>
              </div>
              <div class="grid grid-cols-[repeat(auto-fit,minmax(220px,1fr))] gap-6 p-0">
                <div class="flex flex-1 gap-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-6 flex-col">
                  <span class="material-symbols-outlined text-3xl text-primary">build</span>
                  <div class="flex flex-col gap-1">
                    <h3 class="text-text-light dark:text-text-dark text-lg font-bold leading-tight">Manutenção Geral</h3>
                    <p class="text-text-muted-light dark:text-text-muted-dark text-sm font-normal leading-normal">Trocas de óleo, filtros e fluidos para manter seu carro funcionando sem problemas.</p>
                  </div>
                </div>
                <div class="flex flex-1 gap-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-6 flex-col">
                  <span class="material-symbols-outlined text-3xl text-primary">memory</span>
                  <div class="flex flex-col gap-1">
                    <h3 class="text-text-light dark:text-text-dark text-lg font-bold leading-tight">Diagnóstico de Motor</h3>
                    <p class="text-text-muted-light dark:text-text-muted-dark text-sm font-normal leading-normal">Tecnologia avançada para identificar e resolver problemas de motor rapidamente.</p>
                  </div>
                </div>
                <div class="flex flex-1 gap-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-6 flex-col">
                  <span class="material-symbols-outlined text-3xl text-primary">album</span>
                  <div class="flex flex-col gap-1">
                    <h3 class="text-text-light dark:text-text-dark text-lg font-bold leading-tight">Freios e Suspensão</h3>
                    <p class="text-text-muted-light dark:text-text-muted-dark text-sm font-normal leading-normal">Inspeção e reparo completos para garantir sua segurança na estrada.</p>
                  </div>
                </div>
                <div class="flex flex-1 gap-4 rounded-xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 p-6 flex-col">
                  <span class="material-symbols-outlined text-3xl text-primary">tire_repair</span>
                  <div class="flex flex-col gap-1">
                    <h3 class="text-text-light dark:text-text-dark text-lg font-bold leading-tight">Serviços de Pneus</h3>
                    <p class="text-text-muted-light dark:text-text-muted-dark text-sm font-normal leading-normal">Alinhamento, balanceamento e troca de pneus com equipamentos de precisão.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- How It Works -->
        <section class="py-10 sm:py-20" id="about">
          <div class="max-w-7xl mx-auto px-4 sm:px-10">
            <div class="flex flex-col lg:flex-row items-center gap-12 lg:gap-20">
              <div class="w-full lg:w-1/2">
                <div class="flex flex-col gap-4 max-w-2xl">
                  <h2 class="text-text-light dark:text-text-dark tracking-light text-[32px] font-bold leading-tight sm:text-4xl sm:font-black">Simples, Rápido e Transparente</h2>
                  <p class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal">Nosso processo foi pensado para sua conveniência. Veja como é fácil cuidar do seu carro conosco.</p>
                </div>
                <div class="mt-8 grid grid-cols-[40px_1fr] gap-x-4">
                  <div class="flex flex-col items-center gap-1 pt-3">
                    <span class="material-symbols-outlined text-primary text-3xl">event</span>
                    <div class="w-[2px] bg-gray-300 dark:bg-gray-700 h-full grow"></div>
                  </div>
                  <div class="flex flex-1 flex-col pb-8 pt-2">
                    <p class="text-text-light dark:text-text-dark text-lg font-bold leading-normal">Passo 1: Agende seu horário</p>
                    <p class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal">Use nosso formulário online para escolher o serviço e o melhor horário para você.</p>
                  </div>
                  <div class="flex flex-col items-center gap-1">
                    <div class="w-[2px] bg-gray-300 dark:bg-gray-700 h-2"></div>
                    <span class="material-symbols-outlined text-primary text-3xl">directions_car</span>
                    <div class="w-[2px] bg-gray-300 dark:bg-gray-700 h-full grow"></div>
                  </div>
                  <div class="flex flex-1 flex-col pb-8 pt-3">
                    <p class="text-text-light dark:text-text-dark text-lg font-bold leading-normal">Passo 2: Traga seu carro</p>
                    <p class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal">Venha até nossa oficina na data marcada. Nossa equipe estará pronta para te receber.</p>
                  </div>
                  <div class="flex flex-col items-center gap-1 pb-3">
                    <div class="w-[2px] bg-gray-300 dark:bg-gray-700 h-2"></div>
                    <span class="material-symbols-outlined text-primary text-3xl">check_circle</span>
                  </div>
                  <div class="flex flex-1 flex-col pb-3 pt-3">
                    <p class="text-text-light dark:text-text-dark text-lg font-bold leading-normal">Passo 3: Retire seu veículo</p>
                    <p class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal">Avisaremos assim que o serviço estiver concluído. Seu carro estará pronto e em perfeitas condições.</p>
                  </div>
                </div>
              </div>
              <div class="w-full lg:w-1/2">
                <img class="w-full h-full object-cover rounded-xl aspect-square lg:aspect-auto" data-alt="Mechanic working on a car engine in a clean workshop" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBhzK9fCP2A9suJKuIQPOU524SGMinPSzNpqp-kWQSXIaBTHzMJjsoMB35q4DMo16FgwUOpSzb79_NzgutMGbByqrJD6lIuRUDonfuF66FShzYtQgPBeLnRzJO2Tm5RVbQbAkFtuTUT0fwNtNAWZl1wH9ip2wzAoYtqQXrUdf1U48WBG1mk9U7bOP800rTRdwwHhCkzv5sQ5qsWebf4abnULvgAWQJui3RvmUNbo0BIBKhweIrQX9ICc-j0Rm5BGJNnYnXpmEIR19tJ"/>
              </div>
            </div>
          </div>
        </section>
        <!-- Reviews -->
        <section class="py-10 sm:py-20 bg-background-light dark:bg-background-dark border-t border-b border-gray-200 dark:border-gray-800">
          <div class="max-w-7xl mx-auto px-4 sm:px-10">
            <div class="flex flex-col gap-10">
              <div class="flex flex-col gap-4 max-w-3xl text-center mx-auto">
                <h2 class="text-text-light dark:text-text-dark tracking-light text-[32px] font-bold leading-tight sm:text-4xl sm:font-black">O Que Nossos Clientes Dizem</h2>
                <p class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal">A confiança e a satisfação dos nossos clientes são nossa maior prioridade.</p>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="flex flex-col gap-4 bg-white dark:bg-gray-900 p-6 rounded-xl border border-gray-200 dark:border-gray-800">
                  <div class="flex items-center gap-4">
                    <img class="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-12 object-cover" data-alt="Profile picture of João Silva" src="https://lh3.googleusercontent.com/aida-public/AB6AXuD9P_iMCphr8z_JM9EmAe55Bz258PabsmZMOj6SeouDQkGvIrConjkcZ9D6q5s4Qk3aLaMv8jVz8ZnYY5x9N5mmVW6CEJETzDcHiTYk9QI7NrY-qcl0FcBPW7K3gNw5wXR9NG5W2335YNrmsSwtCIcuBH6uFy6SdZ-r_nTS5Ql5FMNnro_lpP4sDwcwOvXtHiU-q_fLaGLkuf-h61J4h8XDsEG1D0zNJ8EeOGlnxFmNCpkvlBk91jbWVMDcXdX9V-3ZwItzQGYKgqvt"/>
                    <div class="flex-1">
                      <p class="text-text-light dark:text-text-dark text-base font-bold leading-normal">João Silva</p>
                      <p class="text-text-muted-light dark:text-text-muted-dark text-sm font-normal leading-normal">15 de Março, 2024</p>
                    </div>
                  </div>
                  <div class="flex gap-0.5 text-primary">
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                  </div>
                  <p class="text-text-light dark:text-text-dark text-base font-normal leading-normal">Atendimento excepcional e transparente. Meu carro nunca esteve tão bem cuidado. O profissionalismo da equipe é notável, recomendo a todos!</p>
                </div>
                <div class="flex flex-col gap-4 bg-white dark:bg-gray-900 p-6 rounded-xl border border-gray-200 dark:border-gray-800">
                  <div class="flex items-center gap-4">
                    <img class="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-12 object-cover" data-alt="Profile picture of Maria Oliveira" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAeggF4jKcPxakaphgfIhySmdB5vRlpITYFCsTkqZR2HD3cNKgZtSNV9FEL1GDgUXr51DReYpBxNJ5rsC6PgpQMIxIFpCpwWzQ2x5OfbmufE2rczhOONFJE3TCdHAvaAm7H4vQOIHgJf7bxTlq5Dao9_ajrcGNJ686hAUHdeQt6jCtG-TNVf8W3y7OQ8De3oHd66KzkUjlvAb4z8OcC59A7C4_OeZl1-WtrX0mM0uvMjVp7eglQX2rROVYEwrWeLqv6riqOxBJ6l3C4"/>
                    <div class="flex-1">
                      <p class="text-text-light dark:text-text-dark text-base font-bold leading-normal">Maria Oliveira</p>
                      <p class="text-text-muted-light dark:text-text-muted-dark text-sm font-normal leading-normal">2 de Fevereiro, 2024</p>
                    </div>
                  </div>
                  <div class="flex gap-0.5 text-primary">
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                    <span class="material-symbols-outlined !text-xl" style="font-variation-settings: 'FILL' 1">star</span>
                  </div>
                  <p class="text-text-light dark:text-text-dark text-base font-normal leading-normal">Serviço rápido, preço justo e de altíssima qualidade. Fiquei muito satisfeita com o reparo e com a clareza nas explicações do mecânico.</p>
                </div>
              </div>
            </div>
          </div>
        </section>
        <!-- Contact & Scheduling Form -->
        <section class="py-10 sm:py-20" id="contact">
          <div class="max-w-7xl mx-auto px-4 sm:px-10">
            <div class="flex flex-col gap-10 items-center">
              <div class="flex flex-col gap-4 max-w-3xl text-center">
                <h2 class="text-text-light dark:text-text-dark tracking-light text-[32px] font-bold leading-tight sm:text-4xl sm:font-black">Agende Seu Horário</h2>
                <p class="text-text-muted-light dark:text-text-muted-dark text-base font-normal leading-normal">Preencha o formulário abaixo para agendar seu serviço. Entraremos em contato para confirmar.</p>
              </div>
                <div class="w-full max-w-3xl">
                    <agendamento-form />
                </div>
            </div>
          </div>
        </section>
      </main>
      <!-- Footer -->
      <footer class="bg-text-light dark:bg-background-dark text-background-light dark:text-text-dark border-t border-gray-200 dark:border-gray-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-10 py-10">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="md:col-span-2">
              <div class="flex items-center gap-4">
                <span class="material-symbols-outlined text-3xl text-primary">directions_car</span>
                <h2 class="text-xl font-bold">AutoExpert</h2>
              </div>
              <p class="mt-4 text-sm text-gray-400 dark:text-text-muted-dark max-w-sm">Sua oficina de confiança, combinando expertise tradicional com tecnologia moderna para o cuidado completo do seu veículo.</p>
            </div>
            <div>
              <h3 class="font-bold tracking-wider uppercase text-sm text-white dark:text-text-dark">Links Rápidos</h3>
              <ul class="mt-4 space-y-2">
                <li><a class="text-sm text-gray-400 dark:text-text-muted-dark hover:text-primary transition-colors" href="#services">Serviços</a></li>
                <li><a class="text-sm text-gray-400 dark:text-text-muted-dark hover:text-primary transition-colors" href="#about">Sobre Nós</a></li>
                <li><a class="text-sm text-gray-400 dark:text-text-muted-dark hover:text-primary transition-colors" href="#contact">Contato</a></li>
              </ul>
            </div>
            <div>
              <h3 class="font-bold tracking-wider uppercase text-sm text-white dark:text-text-dark">Contato</h3>
              <ul class="mt-4 space-y-2 text-sm text-gray-400 dark:text-text-muted-dark">
                <li>Rua Fictícia, 123 - Cidade</li>
                <li>(11) 99999-8888</li>
                <li>contato@autoexpert.com</li>
                <li>Seg-Sex: 8h - 18h</li>
              </ul>
            </div>
          </div>
          <div class="mt-8 pt-8 border-t border-gray-700 dark:border-gray-700 text-center text-sm text-gray-500 dark:text-text-muted-dark">
            <p>© 2024 AutoExpert. Todos os direitos reservados.</p>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import AgendamentoForm from '@/components/AgendamentoForm.vue'

export default {
  name: 'Landing',
  components: {
    AgendamentoForm
  }
}
</script>

<style scoped></style>
