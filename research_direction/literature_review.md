# 智能体自动挖掘跨模态协同感知风险：文献综述

**日期**: 2026年10月24日
**研究方向**: 智能体自动发现融合风险与跨模态错误传播

---

## 摘要

本综述系统梳理了2025-2026年跨模态融合风险、智能体自动科研系统和自动漏洞挖掘三个领域的最新进展，并分析了这些工作如何支撑"智能体自动挖掘跨模态协同感知风险"这一研究方向。综述发现：多模态融合风险研究已从单一模态扰动转向错误传播路径的诊断，智能体自动科研系统已实现端到端的假设-实验-分析闭环，自动漏洞挖掘正从输入生成转向证据驱动的缺陷归因。这些进展为智能体自动发现融合失效、区分失效原因并指导修复提供了方法论基础。

---

## 一、跨模态融合风险与错误传播

### 1.1 研究现状：从噪声大小到传播路径

近期研究明确指出，多模态融合的核心风险不只是单模态受损，而是错误沿着不对称的跨模态交互路径被放大并进入最终决策。传统鲁棒性研究往往将失效简化为最终任务性能下降或总扰动幅度，但新工作表明，严重失效取决于扰动是否命中承担主要功能的有向交互路径，而非总扰动量 [[Liu26al]](https://doi.org/10.1145/3776574.3831152)。

#### 1.1.1 传播机制建模

**Che26bd** 提出将多模态鲁棒性重新框架化为扰动传播问题，并将其建模为受控状态演化系统。该研究引入了融合路径对抗攻击（FPAA）来分析融合路径敏感性，并提出了双振荡Mamba融合网络，通过收缩约束的状态空间演化和token级、决策级振荡调节来限制扰动增益，同时保持跨模态一致性 [[Che26bd]](https://doi.org/10.1038/s41598-026-65896-5)。

**Liu26al** 在36种受控退化和6个MulT设置下对通道退化进行了系统研究，发现严重失效是有条件的而非均匀的。五级回溯显示，关键损伤信号在记忆块之前形成：路径级扰动比总扰动更好地解释退化，而记忆模块主要锐化已有的不对称信号而非成为主要预测阶段。该研究提出了可靠性设计原则：当鲁棒性预算有限时，系统应保护锚定主导交互结构的通道和方向，而非均匀硬化所有模态 [[Liu26al]](https://doi.org/10.1145/3776574.3831152)。

#### 1.1.2 模态破坏与诊断框架

**Zha25aa** 引入了"模态破坏"（modality sabotage）这一诊断失效模式，即高置信度的单模态错误覆盖其他证据并误导融合结果。该研究提出了一个轻量级、模型无关的评估层，将每个模态视为一个智能体，产生候选标签和简短自评估用于审计。简单的融合机制聚合这些输出，暴露贡献者（支持正确结果的模态）和破坏者（误导融合结果的模态）。在多模态情感识别基准上的案例研究揭示了系统性的可靠性特征，提供了失效可能源于数据集伪影或模型限制的洞察 [[Zha25aa]](https://doi.org/10.48550/arXiv.2511.02794)。

**Din25c** 提供了动态多模态融合加剧模态贪婪的理论证明。该研究观察到动态融合在训练过程中加剧模型的贪婪倾向，导致模型不能充分利用低质量模态。该理论分析强调了在采用动态多模态学习时需要警惕贪婪风险 [[Din25c]](https://doi.org/10.1145/3746027.3754820)。

#### 1.1.3 分布鲁棒性与不确定性量化

**Yan25l** 提出了分布鲁棒多模态机器学习的新框架，研究编码器特定错误传播。该研究建立了泛化上界和极小极大下界，提供性能保证，这些结果在考虑编码器特定错误传播的设置中进一步扩展。实证结果表明，该方法在模拟设置和真实世界数据集上都提高了鲁棒性 [[Yan25l]](https://doi.org/10.48550/arXiv.2511.05716)。

**Che25y** 提出了HyperDUM，一种利用超维计算高效量化特征层认知不确定性的确定性不确定性方法（DUM）。该方法通过通道和patch-wise投影和打包技术捕获通道和空间不确定性，然后自适应加权多模态传感器特征以减轻不确定性传播并改善特征融合。在3D目标检测和语义分割任务上，HyperDUM平均比SOTA方法提升2.01%/1.27%，同时需要2.36倍更少的浮点运算和最多38.30倍更少的参数 [[Che25y]](https://doi.org/10.1109/CVPR52734.2025.02078)。

#### 1.1.4 计算机视觉与自动驾驶应用

**Gan26c** 评估了相机-4D雷达融合在传感器退化下的测试时鲁棒性。在View-of-Delft数据集上评估了SGDet3D在六种退化下的表现。结果显示检测器对图像变暗和雷达点丢失保持鲁棒，即使移除50%的雷达点，mAP下降不到4分。相比之下，相机高斯噪声和雷达测量噪声造成严重损害。在重度水平下，相机噪声将mAP从59.75降至27.09，RCS噪声降至14.35。研究发现未来工作应更多关注测量级噪声而非点稀疏性 [[Gan26c]](https://doi.org/10.1109/IWIS70716.2026.11667732)。

**Par25c** 提出了MoME，一种通过混合专家方法实现鲁棒性能的LiDAR-相机3D目标检测器。MoME使用三个并行专家解码器，分别使用相机特征、LiDAR特征或两者组合来解码对象查询。自适应查询路由器（AQR）根据相机和LiDAR特征的质量为每个查询选择最合适的专家解码器。在nuScenes-R基准上的评估显示，MoME在极端天气和传感器故障条件下实现了SOTA性能 [[Par25c]](https://doi.org/10.1109/CVPR52734.2025.00630)。

**Sha25e** 提出了DEJAVU攻击，利用车载网络操纵时间完整性并创建细微的时间错位，严重降级下游多模态感知任务。跨不同模型和数据集的综合攻击分析揭示了传感器的任务特定不平衡敏感性：目标检测过度依赖LiDAR输入，而目标跟踪高度依赖相机输入。单帧LiDAR延迟可将车辆检测mAP降低88.5%，三帧相机延迟使车辆跟踪MOTA下降73% [[Sha25e]](https://doi.org/10.1109/SaTML68715.2026.00042)。

#### 1.1.5 多模态大语言模型的模态偏差

**Sel26** 对音视频大语言模型（AVLLMs）进行了首次机制可解释性研究，分析音频和视觉特征如何通过不同层演化并融合以产生最终文本输出。研究发现，虽然AVLLM在中间层编码了丰富的音频语义，但当音频与视觉冲突时，这些能力很大程度上无法在最终文本生成中浮现。探测分析显示，有用的潜在音频信息存在，但更深层的融合层不成比例地偏向视觉表征，这倾向于抑制音频线索。这种不平衡可追溯到训练：AVLLM的音频行为与其视觉-语言基础模型高度匹配，表明对音频监督的额外对齐有限 [[Sel26]](https://doi.org/10.1109/CVPRF71909.2026.00566)。

### 1.2 研究空白与本文方向的关联

当前跨模态融合风险研究存在以下关键空白：

1. **路径级误差归因不足**：现有研究开始意识到路径级扰动比总扰动更重要，但缺乏系统化的路径级误差归因方法。您的研究方向强调"区分模态权重失衡、时间对应失效、交互模块改变表征"三种竞争假设，正好填补这一空白。

2. **无线感知领域的直接量化工作较少**：相比于计算机视觉和自动驾驶，无线感知领域直接量化"误差如何跨模态传播"的工作较少。您的研究聚焦Wi-Fi+毫米波动作识别，正好是这一领域的空白填补。

3. **竞争假设验证机制缺失**：现有研究多关注发现失效，但缺乏系统化的竞争假设验证机制。您的研究方向设计"让智能体选择实验，区分不同解释"，这是对现有方法的重要推进。

---

## 二、智能体自动科研系统

### 2.1 研究现状：从单项辅助到端到端闭环

2025-2026年的核心进展是将科研从"单项辅助"推进到可迭代的假设-实验-分析闭环，但可靠能力仍主要出现在边界明确、结果可验证的任务中。

#### 2.1.1 端到端计算科研

**Yam26** 在Nature发表论文，提出了完全自动化科学过程的管道。AI Scientist创建研究想法、编写代码、运行实验、绘制和分析数据、撰写完整的科学手稿，并执行自己的同行评审。其想法、执行和展示的质量足以让该系统生成的手稿通过顶级机器学习会议研讨会的第一轮同行评审（接受率70%） [[Yam26]](https://doi.org/10.1038/s41586-026-10265-5)。

**Yam25** 提出了AI Scientist-v2，通过渐进式智能体树搜索方法论实现了研讨级自动化科学发现。与v1相比，v2消除了对人类编写代码模板的依赖，有效泛化到多样化的机器学习领域，并集成了视觉语言模型反馈循环以迭代改进图表的内容和美学。评估表明，三篇完全自主提交的手稿中，有一篇超过了人类平均接受阈值，标志着第一篇完全AI生成的论文成功通过同行评审 [[Yam25]](https://doi.org/10.48550/arXiv.2504.08066)。

**Gao26k** 提出了AutoScientists，一个用于长期运行计算科学实验的去中心化智能体团队。智能体解释共享实验状态，围绕有前景的假设自组织成团队，在使用实验计算前批评提案，并分享成功和失败以减少冗余探索。在BioML-Bench、GPT训练优化和ProteinGym适应度预测上，AutoScientists显著优于先前的AI智能体 [[Gao26k]](https://doi.org/10.48550/arXiv.2605.28655)。

#### 2.1.2 实验闭环与领域系统

**Mit25b** 提出了Kosmos，一个通过结构化世界模型连接文献检索和数据分析的AI科学家，支持长时程、多轮发现并追溯报告主张。Kosmos在每次运行中平均执行42,000行代码并阅读1,500篇论文，独立科学家发现79.4%的陈述准确，单一20周期Kosmos运行平均相当于6个月的人类研究时间 [[Mit25b]](https://doi.org/10.48550/arXiv.2511.02824)。

**Got25** 在Nature发表论文，提出了Co-Scientist，一个基于Gemini的结构化科学思考和假设生成的多智能体AI系统。Co-Scientist旨在帮助科学家发现新的原创知识。该系统的设计包括多智能体架构和异步任务执行框架，以及锦标赛演化过程以实现自我改进的假设生成。在生物医学应用中的实际验证表明，Co-Scientist帮助识别了新的药物重定位候选和协同组合疗法 [[Got25]](https://doi.org/10.1038/s41586-026-10644-y)。

**Gha26b** 在Nature发表论文，提出了Robin，一个能够完全自动化假设生成和数据分析的实验生物学多智能体系统。通过整合文献搜索智能体与数据分析智能体，Robin能够生成假设、提出实验、解释实验结果并生成更新假设，实现半自主的科学发现。通过应用该系统，识别了干性年龄相关性黄斑变性的有前景的治疗候选ripasudil和KL001，并验证了体外功效 [[Gha26b]](https://doi.org/10.1038/s41586-026-10652-y)。

**Swa25** 在Nature发表论文，展示了AI智能体设计的虚拟实验室能够设计新的SARS-CoV-2纳米抗体。该研究展示了LLM与实验室工作流的成功集成，标志着按需自主化学研究的能力 [[Swa25]](https://doi.org/10.1038/s41586-025-09442-9)。

#### 2.1.3 长程探索与共享实验记忆

**Wen25g** 提出了DeepScientist，一个通过月级时间线进行目标导向、完全自主科学发现的系统。该系统将发现形式化为贝叶斯优化问题，通过"假设、验证、分析"的分层评估过程实现。消耗超过20,000 GPU小时，系统生成了约5,000个独特的科学想法并实验验证了约1,100个，最终在三个前沿AI任务上超越了人类设计的SOTA方法 [[Wen25g]](https://doi.org/10.48550/arXiv.2509.26603)。

**Sch25f** 提出了Agent Laboratory，一个能够完成整个研究过程的自主LLM框架。该框架接受人类提供的研究想法，通过文献综述、实验和报告撰写三个阶段产生综合研究输出，包括代码仓库和研究报告，同时允许用户在每个阶段提供反馈和指导。评估发现o1-preview驱动的Agent Laboratory产生最佳研究结果，生成的机器学习代码能达到与现有方法相当的SOTA性能，人类参与在每个阶段提供反馈显著提高整体研究质量，研究费用比之前的自主研究方法降低84% [[Sch25f]](https://doi.org/10.18653/v1/2025.findings-emnlp.320)。

### 2.2 研究空白与本文方向的关联

智能体自动科研系统为您的方向提供了以下关键方法论支撑：

1. **假设演化与竞争假设生成**：Co-Scientist的锦标赛演化过程为您的"竞争假设选择干预实验"提供了直接的方法论参考。您的研究可以将竞争假设（模态权重失衡 vs 时间对应失效 vs 交互模块改变表征）作为演化目标，让智能体选择最有区分力的实验。

2. **实验闭环与反馈利用**：AutoScientists的共享实验状态和失败经验累积机制，为您的"可复现证据积累记忆"提供了实现模板。您可以累积"哪些风险已经发现、哪些解释被否定、哪些干预有效"的记忆。

3. **机制评价反馈**：Kosmos和Robin的证据溯源机制为您的"机制评价"提供了参考。不同于模型评价（LLM认为假设是否合理）和性能评价（实验指标是否提高），机制评价关注实验是否支持某种解释并排除其他解释。

### 2.3 与您研究规划的对应关系

| 您的研究规划元素 | 对应的智能体科研系统 | 方法论迁移路径 |
|-----------------|------------------|--------------|
| 假设生成与演化 | Co-Scientist (锦标赛演化) | 将三种竞争假设作为演化目标，通过实验反馈选择最优解释 |
| 可执行实验驱动 | AI Scientist-v2 (树搜索), DeepScientist (贝叶斯优化) | 将"测试一种扰动—分析现象—追加干预"组织成实验树 |
| 受限环境中的持续优化 | Karpathy autoresearch | 建立可重复、预算明确的无线模型测试环境 |
| 长期探索与共享实验记忆 | AutoScientists, Kosmos | 累积"哪些风险已发现、哪些解释被否定、哪些干预有效"的记忆 |

---

## 三、自动漏洞挖掘与模型红队

### 3.1 研究现状：从输入生成到证据驱动的缺陷归因

2025-2026年的主线是自动化测试从"让LLM生成输入"转向"用运行反馈闭环搜索、复现并归因"。

#### 3.1.1 深度学习库模糊测试

**Zha26cu** 提出了TransFuzz，利用LLM执行多功能且受控的bug转移以进行深度学习库静默bug模糊测试。该方法从历史bug报告中提取上下文感知的bug模式，使用基于功能的嵌入匹配语义相关的API，并合成具有定制oracle的测试用例。在PyTorch、TensorFlow和MindSpore上的评估成功发现79个未知bug（12个确认为CVE），证明了其在迁移DL库bug发现能力方面的有效性 [[Zha26cu]](https://doi.org/10.1145/3798258)。

**Zha25an** 提出了DFuzz，一个LLM驱动的DL库模糊测试方法。该研究为LLM提供了DL库API的"白盒视图"，使其能够利用LLM的推理和生成能力实现全面模糊测试。在主流DL库上的实验表明，DFuzz能够覆盖比SOTA（基于LLM）模糊器更多的API，成功检测到37个bug，其中8个已被修复，19个已被开发者复现但仍在调查中 [[Zha25an]](https://doi.org/10.1109/ICSE553472025.00041)。

**Qin26f** 提出了FlashFuzz，利用LLM自动合成API级测试harness。该方法结合harness模板、辅助函数和API文档合成harness，并采用反馈驱动策略迭代修复损坏的harness。结果显示，FlashFuzz能够成功为PyTorch和TensorFlow的1,271和786个API合成测试harness，比SOTA技术提高212.88%的覆盖率和5.4倍的有效性，并揭示了54个先前未知的bug [[Qin26f]](https://doi.org/10.1109/ICST69053.2026.00023)。

**Ou25** 提出了MirrorFuzz，利用LLM和共享bug进行深度学习框架API模糊测试。MirrorFuzz在三阶段中操作：首先收集每个API的历史bug数据以识别潜在的buggy API；其次将特定框架中的每个buggy API与框架内和跨其他框架的相似API匹配；第三，利用LLM合成API下的代码，利用相似API的历史bug数据在类比API中触发类比bug。在四个主流DL框架上的评估显示，MirrorFuzz比SOTA方法在TensorFlow和PyTorch上分别提高39.92%和98.20%的代码覆盖率，发现315个bug，262个为新发现，80个已被修复，52个被分配CNVD ID [[Ou25]](https://doi.org/10.1109/TSE.2025.3619966)。

#### 3.1.2 智能体红队与模型诊断

**Zho25k** 提出了AutoRedTeamer，一个用于LLM的完全自动化、端到端红队框架。该框架结合多智能体架构和记忆引导的攻击选择机制，实现新攻击向量的持续发现和集成。双智能体框架包括红队智能体和策略提议智能体，前者可以仅从高级风险类别生成和执行测试用例，后者通过分析近期研究自主发现和实施新攻击。在HarmBench上评估显示，AutoRedTeamer在Llama-3.1-70B上实现20%更高的攻击成功率，同时将计算成本降低46% [[Zho25k]](https://doi.org/10.48550/arXiv.2503.15754)。

**Wu26aj** 提出了ChainFuzzer，一个用于发现和复现LLM智能体中工作流级多工具漏洞的灰盒模糊测试框架。ChainFuzzer识别具有严格源到汇数据流证据的高影响操作，并基于跨工具依赖提取合理的上游候选工具链；使用轨迹引导提示求解（TPS）合成稳定提示以可靠驱动智能体执行目标链；执行守卫感知模糊测试以在LLM守卫下通过负载变异和汇特定oracle复现漏洞。在20个流行的开源LLM智能体应用上评估确认了365个独特的、可复现的漏洞，跨越19/20个应用（302个需要多工具执行） [[Wu26aj]](https://doi.org/10.48550/arXiv.2603.12614)。

**Fen26m** 提出了Vera，一个通过三阶段自强化管道将软件工程测试原则实例化到非确定性智能体的端到端自动化安全测试框架。第一阶段通过文献驱动的探索持续发现并将新兴风险结构化为安全风险、攻击方法和工具执行环境的分类法；第二阶段通过分类法维度的组合产生可执行安全用例；第三阶段在隔离沙箱中运行异构智能体，其中控制智能体基于运行时观察引导多轮交互，而证据根基验证器从环境状态和工具调用证据而非模型自报告判断结果 [[Fen26m]](https://doi.org/10.48550/arXiv.2607.01793)。

**Mao26d** 提出了Agent Hacks Agents (AHA)，通过Karpathy风格的autoresearch循环在智能体轨迹上测试可证假设来发现漏洞概念。AHA保留漏洞概念，每个概念说明攻击为何成功、启用条件以及反驳证据。重复确认的概念进入漏洞概念图，连接相关弱点。在18个设置、三个受害模型和两个智能体上，概念分为八个家族。在保持实例上概念达到47.0%攻击成功率（而最强基线为32.8%），同时修补每个概念的启用条件将AgentHazard ASR降低41.11分 [[Mao26d]](https://arxiv.org/abs/2607.11698)。

#### 3.1.3 ML缺陷诊断

**Jah25** 提出了DEFault（Detect and Explain Fault），一种检测和诊断DNN程序故障的新技术。该方法首先在模型训练期间捕获动态特征，利用分层分类方法检测文献中的所有主要故障类别，然后从DNN程序中捕获静态特征（如层类型），并利用可解释AI方法（如SHAP）缩小根本原因。在约14.5K DNN程序的数据集和52个真实故障DNN程序的基准数据集上评估，DEFault在检测真实世界故障DNN程序上达到约94%的召回率，在诊断根本原因上达到约63%的召回率 [[Jah25]](https://doi.org/10.1109/ICSE55347.2025.00224)。

**Jah26b** 提出了DEFault++，一种首先检测故障，然后识别受影响组件，最后识别其中原因的分层学习技术。DEFault++用故障传播图（FPG）组织组件级运行时测量，架构依赖路径的结构先验，并报告每个诊断背后的证据。构建了DEFault-bench，涵盖七个模型、九个任务以及编码器和解码器架构的5,556个标记运行。在开发者研究中，DEFault++将修复准确性从57.1%提高到83.3% [[Jah26b]](https://arxiv.org/abs/2604.28118)。

### 3.2 研究空白与本文方向的关联

自动漏洞挖掘为您的方向提供了以下关键方法论支撑：

1. **可复现反例缩减**：漏洞挖掘中的最小复现样例（minimally reproducible example）概念，对应您研究中的"缩减触发条件并验证路径"。您的研究应该输出明确的触发条件，如"在指定模型和样本上，某个短时间片的受限变化足以触发融合错误"。

2. **干预实验与竞争假设**：Mao26d的漏洞概念图和验证机制，为您的"竞争假设选择干预实验"提供了参考。您可以借鉴其"目标干预与随机干预的差异，竞争解释被区分的程度"的评价方法。

3. **证据根基验证**：Fen26m的证据根基验证机制，为您的"证据支撑的攻击链重建"提供了参考。您的智能体应该基于可观察的证据而非模型自报告来判断实验结果。

### 3.3 与您研究规划的对应关系

| 您的研究规划元素 | 对应的漏洞挖掘方法 | 方法论迁移路径 |
|-----------------|-----------------|--------------|
| 缩减触发条件并验证路径 | 最小复现样例，变体分析 | 从成功样例中逐步减小扰动强度、减少受影响时间片、删除冗余扰动组合 |
| 竞争假设选择干预实验 | 漏洞概念图，假设验证 | 设计区分不同假设的干预实验，记录支持和削弱它们的实验 |
| 证据根基验证 | 证据根基验证器 | 基于可观察的环境状态和工具调用证据判断实验结果，而非模型自报告 |

---

## 四、综合分析与研究方向定位

### 4.1 现有工作的局限性

尽管上述三个领域都取得了显著进展，但在"智能体自动挖掘跨模态协同感知风险"这一交叉方向上仍存在以下局限性：

1. **跨模态融合风险的系统化诊断不足**：现有研究开始认识到路径级误差传播的重要性，但缺乏系统化的诊断框架来区分不同的失效原因（模态权重失衡、时间对应失效、交互模块改变表征）。

2. **智能体用于多模态风险发现的研究很少**：智能体科研系统和漏洞挖掘工具大多针对单一模态或纯文本/代码场景，尚未系统应用于多模态无线感知的融合风险发现。

3. **竞争假设验证机制缺失**：现有工作多为单向发现失效或攻击，缺乏系统化的竞争假设生成和验证机制来区分不同的失效原因。

4. **无线感知领域的直接应用不足**：大量研究集中在计算机视觉和自动驾驶，无线感知领域的直接应用研究较少，特别是Wi-Fi+毫米波动作识别。

### 4.2 本研究的独特贡献

基于上述分析，您的研究方向具有以下独特贡献：

1. **方法论创新**：首次将智能体自动科研、自动漏洞挖掘和多模态融合风险诊断三个领域的方法论整合，形成"发现失效-验证机制-指导修复"的递进贡献。

2. **领域特色**：聚焦无线感知（Wi-Fi+毫米波动作识别），填补了该领域在智能体驱动风险发现方面的空白。

3. **评估体系创新**：提出以"区分解释"为目标的智能体评估指标，而非传统的攻击成功率或论文生成质量，更符合科学问题的本质。

4. **理论结合实践**：既有理论框架（融合风险数学定义、竞争假设），又有实践路径（XRF55实验底座、扰动工具库、验证器设计）。

### 4.3 与您研究规划的对应关系

您的研究规划文档中的工作流与现有文献存在明确的对应关系：

| 规划步骤 | 对应文献支撑 | 实现路径 |
|---------|------------|---------|
| 建立能支持诊断的实验底座 | 多模态融合对比模型（单模态、分数融合、特征拼接、显式交互） | 使用XRF55实现，参考现有工作 |
| 明确什么算"有效测试" | 有效测试约束、验证器设计 | 借鉴DL库模糊测试的oracle设计 |
| 智能体决定"测什么" | 智能体决策、数值搜索分离 | LLM决策测试策略，优化器处理连续参数 |
| 成功样例缩减为可复现触发条件 | 最小复现样例、变体分析 | 借鉴漏洞挖掘的变体分析思路 |
| 竞争假设选择干预实验 | 竞争假设生成、锦标赛演化 | 借鉴Co-Scientist的锦标赛演化机制 |
| 根据验证结果设计修复 | 漏洞修复、推广性检查 | 借鉴漏洞挖掘的修复验证机制 |

---

## 五、总结与展望

### 5.1 研究意义

本研究方向将智能体自动科研、自动漏洞挖掘和多模态融合风险诊断三个前沿领域的方法论进行交叉融合，首次系统性地探索智能体在无线感知领域的融合风险自动发现、诊断和修复。这不仅对多模态感知鲁棒性具有重要理论意义，也对自动驾驶、机器人感知等安全关键应用具有实际价值。

### 5.2 可行性评估

基于现有文献分析，本研究方向的可行性体现在：

1. **方法论的成熟度**：三个领域的核心方法论已相对成熟，交叉融合有明确的技术路径。
2. **实验环境的可用性**：XRF55等开源实现提供了可靠的实验底座。
3. **评估指标的可定义性**：区分解释的能力可以通过控制实验进行量化评估。
4. **基线方法的清晰性**：现有方法提供了明确的对照基线（随机搜索、贝叶斯优化、覆盖引导测试等）。

### 5.3 预期挑战

1. **计算资源需求**：智能体搜索和数值优化需要大量计算资源。
2. **实验设计的复杂性**：无线感知的真实实验验证具有挑战性，初期可能需要主要依靠离线模拟。
3. **评估标准的主观性**：区分解释的实验设计本身需要 careful design to avoid 引入新的主观偏见。
4. **泛化性验证**：在未见扰动、其他主体或模型上的泛化性验证需要大量额外工作。

### 5.4 后续工作建议

1. **第一阶段（3-6个月）**：建立实验底座，找到"健康模态仍然正确、融合却出错"的稳定样例，设计能够区分两种原因的实验。
2. **第二阶段（6-12个月）**：引入智能体，研究对象、验证标准和智能体的实际作用，评估其在发现效率、诊断能力和修复指导方面的增益。
3. **第三阶段（12-18个月）**：扩展到更多模态组合、更复杂的风险类型，并探索在真实无线环境中的验证。

---

## 六、参考文献

### 6.1 跨模态融合风险与错误传播

1. Chen, G., Liao, Y., Zhu, X., Zhou, R., & Teng, Y. (2026). Modeling and stabilizing perturbation propagation in multimodal learning via oscillatory state-space dynamics. *Scientific Reports*. https://doi.org/10.1038/s41598-026-65896-5 [[Che26bd]](https://doi.org/10.1038/s41598-026-65896-5)

2. Liu, B., Xiao, Z.-X., & Liu, Z.-P. (2026). When Cross-Modal Attention Fails under Channel Degradation: Diagnosing Dominant Interaction Structure for Reliable Multimodal Interaction. *Proceedings of the 28th International Conference On Multimodal Interaction*. https://doi.org/10.1145/3776574.3831152 [[Liu26al]](https://doi.org/10.1145/3776574.3831152)

3. Zhang, C., Kim, M., Ghorbani, S., Wu, J.-Y., Picard, R. W., Maes, P., & Liang, P. (2025). When One Modality Sabotages the: A Diagnostic Lens on Multimodal Reasoning. *arXiv preprint*. https://doi.org/10.48550/arXiv.2511.02794 [[Zha25aa]](https://doi.org/10.48550/arXiv.2511.02794)

4. Ding, X., Ma, H., & Zhang, C. (2025). A Theoretical Proof of Dynamic Multimodal Fusion Exacerbates Modality Greedy. *Proceedings of the 33rd ACM International Conference on Multimedia*. https://doi.org/10.1145/3746027.3754820 [[Din25c]](https://doi.org/10.1145/3746027.3754820)

5. Yang, P., & Ma, Y. (2025). Distributionally Robust Multimodal Machine Learning. *arXiv preprint*. https://doi.org/10.48550/arXiv.2511.05716 [[Yan25l]](https://doi.org/10.48550/arXiv.2511.05716)

6. Chen, L., Wang, J., Mortlock, T., Khargonekar, P. P., & Al Faruque, M. A. (2025). Hyperdimensional Uncertainty Quantification for Multimodal Uncertainty Fusion in Autonomous Vehicles Perception. *2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 22306–22316. https://doi.org/10.1109/CVPR52734.2025.02078 [[Che25y]](https://doi.org/10.1109/CVPR52734.2025.02078)

7. Gan, Q., Jung, J., Choi, J., & Jo, K. (2026). Robustness Evaluation of Camera–4D Radar Fusion under Sensor Corruptions. *2026 International Workshop on Intelligent Systems (IWIS)*, 1–6. https://doi.org/10.1109/IWIS70716.2026.11667732 [[Gan26c]](https://doi.org/10.1109/IWIS70716.2026.11667732)

8. Park, K., Kim, Y., Kim, D., & Choi, J. (2025). Resilient Sensor Fusion under Adverse Sensor Failures via Multi-Modal Expert Fusion. *2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 6720–6729. https://doi.org/10.1109/CVPR52734.2025.00630 [[Par25c]](https://doi.org/10.1109/CVPR52734.2025.00630)

9. Shahriar, M., Al Barat, M. M., Sundar, H., Zhang, N., Ramakrishnan, N., Hou, Y., & Lou, W. (2025). Temporal Misalignment Attacks against Multimodal Perception in Autonomous Driving. *2026 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)*, 637–655. https://doi.org/10.1109/SaTML68715.2026.00042 [[Sha25e]](https://doi.org/10.1109/SaTML68715.2026.00042)

10. Selvakumar, R., Jayakumar, K., Sakshi, S., Ghosh, S., Gao, R., & Manocha, D. (2026). Do Audio-Visual Large Language Models Really See and Hear? *2026 IEEE/CVF Conference on Computer Vision and Pattern Recognition- FINDINGS Track (CVPRF)*, 5895–5905. https://doi.org/10.1109/CVPRF71909.2026.00566 [[Sel26]](https://doi.org/10.1109/CVPRF71909.2026.00566)

### 6.2 智能体自动科研系统

11. Yamada, Y., Lange, R., Lu, C., Lu, C., Hu, S., Foerster, J., ... & Clune, J. (2026). Towards end-to-end automation of AI research. *Nature*, 914–919. https://doi.org/10.1038/s41586-026-10265-5 [[Yam26]](https://doi.org/10.1038/s41586-026-10265-5)

12. Yamada, Y., Lange, R., Lu, C., Lu, C., Hu, S., Foerster, J., ... & Ha, D. (2025). The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. *arXiv preprint*. https://doi.org/10.48550/arXiv.2504.08066 [[Yam25]](https://doi.org/10.48550/arXiv.2504.08066)

13. Gao, S., Fang, A., & Zitnik, M. (2026). AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation. *arXiv preprint*. https://doi.org/10.48550/arXiv.2605.28655 [[Gao26k]](https://doi.org/10.48550/arXiv.2605.28655)

14. Mitchener, L., Yiu, A., Chang, B., Bourdenx, M., Nadolski, T., Sulovari, A., ... & White, A. D. (2025). Kosmos: An AI Scientist for Autonomous Discovery. *arXiv preprint*. https://doi.org/10.48550/arXiv.2511.02824 [[Mit25b]](https://doi.org/10.48550/arXiv.2511.02824)

15. Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Sirković, P., Myaskovsky, A., ... & Natarajan, V. (2025). Accelerating scientific discovery with Co-Scientist. *Nature*, 487–496. https://doi.org/10.1038/s41586-026-10644-y [[Got25]](https://doi.org/10.1038/s41586-026-10644-y)

16. Ghareeb, A., Chang, B., Mitchener, L., Yiu, A., Szostkiewicz, C. J., Shved, D., ... & Rodriques, S. G. (2026). A multi-agent system for automating scientific discovery. *Nature*, 497–505. https://doi.org/10.1038/s41586-026-10652-y [[Gha26b]](https://doi.org/10.1038/s41586-026-10652-y)

17. Swanson, K., Wu, W., Bulaong, N. L., Pak, J. E., & Zou, J. Y. (2025). The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies. *Nature*, 716–723. https://doi.org/10.1038/s41586-025-09442-9 [[Swa25]](https://doi.org/10.1038/s41586-025-09442-9)

18. Schmidgall, S., Su, Y.-S., Wang, Z., Sun, X.-M., Wu, J.-L., Yu, X.-D., ... & Barsoum, E. (2025). Agent Laboratory: Using LLM Agents as Research Assistants. *Conference on Empirical Methods in Natural Language Processing*, 5977–6043. https://doi.org/10.18653/v1/2025.findings-emnlp.320 [[Sch25f]](https://doi.org/10.18653/v1/2025.findings-emnlp.320)

19. Feng, S.-Y., Ma, R.-M., Yan, X.-Y., Fan, Y., Hu, Y., Huang, S.-T., ... & Bai, L. (2026). InternAgent-1.5: A Unified Agentic Framework for Long-Horizon Autonomous Scientific Discovery. *arXiv preprint*. https://arxiv.org/abs/2602.08990 [[Fen26i]](https://arxiv.org/abs/2602.08990)

20. Ghareeb, A., Chang, B., Mitchener, L., Yiu, A., Szostkiewicz, C. J., Laurent, J. M., ... & Rodriques, S. G. (2025). Robin: A multi-agent system for automating scientific discovery. *arXiv preprint*. https://doi.org/10.48550/arXiv.2505.13400 [[Gha25c]](https://doi.org/10.48550/arXiv.2505.13400)

21. Weng, Y.-X., Zhu, M., Xie, Q.-J., Sun, Q.-Y., Lin, Z., Liu, S., & Zhang, Y. (2025). DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively. *arXiv preprint*. https://doi.org/10.48550/arXiv.2509.26603 [[Wen25g]](https://doi.org/10.48550/arXiv.2509.26603)

22. Tie, G., Shi, J.-W., Song, D., Huang, Y.-X., Sheng, Z., Zhou, X.-Y., ... & Gao, J. (2026). AutoResearch AI: Towards AI-Powered Research Automation for Scientific Discovery. *arXiv preprint*. https://doi.org/10.48550/arXiv.2605.23204 [[Tie26b]](https://doi.org/10.48550/arXiv.2605.23204)

23. Tang, J., Xia, L., Li, Z., & Huang, C. (2025). AI-Researcher: Autonomous Scientific Innovation. *arXiv preprint*. https://doi.org/10.48550/arXiv.2505.18705 [[Tan25d]](https://doi.org/10.48550/arXiv.2505.18705)

24. Wang, X.-M., Xu, J., Lian, S., Chen, Y., Guo, H.-Y., Zhu, F., ... & Liu, C.-L. (2026). The Hitchhiker's Guide to Autonomous Research: A Survey of Scientific Agents. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 15267–15286. https://doi.org/10.1109/TPAMI.2026.3721500 [[Wan26bf]](https://doi.org/10.1109/TPAMI.2026.3721500)

25. Tie, G., Zhou, P., & Sun, L. (2025). A Survey of AI Scientists. *arXiv preprint*. https://doi.org/10.48550/arXiv.2510.23045 [[Tie25]](https://doi.org/10.48550/arXiv.2510.23045)

26. Huang, K.-X., Zhang, S., Wang, H.-C., Qu, Y.-H., Lu, Y., Li, R., ... & Leskovec, J. (2026). Autonomous biomedical research with an artificial intelligence agent. *Science*, eadz4351. https://doi.org/10.1126/science.adz4351 [[Hua26l]](https://doi.org/10.1126/science.adz4351)

27. Villaescusa-Navarro, F., Bolliet, B., Villanueva-Domingo, P., Bayer, A. E., Acquah, C., ... & Zubeldia, Í. (2025). The Denario project: Deep knowledge AI agents for scientific discovery. *arXiv preprint*. https://doi.org/10.48550/arXiv.2510.26887 [[Vil25]](https://doi.org/10.48550/arXiv.2510.26887)

28. Song, T., Luo, M., Zhang, X.-L., Chen, L.-J., Huang, Y., Cao, J., ... & Luo, Y. (2025). A Multiagent-Driven Robotic AI Chemist Enabling Autonomous Chemical Research On Demand. *Journal of the American Chemical Society*. https://doi.org/10.1021/jacs.4c17738 [[Son25c]](https://doi.org/10.1021/jacs.4c17738)

29. Huang, K.-X., Zhang, S., Wang, H.-C., Qu, Y.-H., Lu, Y., Roohani, Y. H., ... & Leskovec, J. (2025). Biomni: A General-Purpose Biomedical AI Agent. *bioRxiv*. https://doi.org/10.1101/2025.05.30.656746 [[Hua25l]](https://doi.org/10.1101/2025.05.30.656746)

30. Wei, J.-Q., Yang, Y.-J., Zhang, X., Chen, Y., Zhuang, X., Gao, Z.-Y., ... & Zhou, B.-W. (2025). From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery. *arXiv preprint*. https://doi.org/10.48550/arXiv.2508.14111 [[Wei25c]](https://doi.org/10.48550/arXiv.2508.14111)

### 6.3 自动漏洞挖掘与模型红队

31. Zhang, K., Xiao, D.-W., Wu, D.-Y., Wang, S., Zhao, J.-L., Lin, Y.-Y., ... & Wang, S.-H. (2026). LLM-Powered Silent Bug Fuzzing in Deep Learning Libraries via Versatile and Controlled Bug Transfer. *Proceedings of the ACM on Programming Languages*, 1599–1626. https://doi.org/10.1145/3798258 [[Zha26cu]](https://doi.org/10.1145/3798258)

32. Zhou, A., Wu, K., Pinto, F., Chen, Z.-R., Zeng, Y., Yang, Y., ... & Li, B. (2025). AutoRedTeamer: Autonomous Red Teaming with Lifelong Attack Integration. *arXiv preprint*. https://doi.org/10.48550/arXiv.2503.15754 [[Zho25k]](https://doi.org/10.48550/arXiv.2503.15754)

33. Wu, J.-R., Yao, Z.-T., Nan, Y., & Zheng, Z.-B. (2026). ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents. *arXiv preprint*. https://doi.org/10.48550/arXiv.2603.12614 [[Wu26aj]](https://doi.org/10.48550/arXiv.2603.12614)

34. Ou, S.-W., Li, Y.-W., Yu, L., Wei, C.-K., Wen, T., Chen, Q., ... & Pan, Z.-L. (2025). MirrorFuzz: Leveraging LLM and Shared Bugs for Deep Learning Framework APIs Fuzzing. *IEEE Transactions on Software Engineering*, 360–375. https://doi.org/10.1109/TSE.2025.3619966 [[Ou25]](https://doi.org/10.1109/TSE.2025.3619966)

35. Feng, Y.-H., Lin, R.-X., Wen, M., He, Q., Guo, Y.-M., Ding, Y.-F., ... & Deng, X.-H. (2026). Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification. *arXiv preprint*. https://doi.org/10.48550/arXiv.2607.01793 [[Fen26m]](https://doi.org/10.48550/arXiv.2607.01793)

36. Zhang, K., Wang, S., Han, J., Zhu, X.-G., Li, X., Wang, S.-H., Wen, S., & Wang, S.-H. (2025). Your Fix Is My Exploit: Enabling Comprehensive DL Library API Fuzzing with Large Language Models. *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*, 3110–3122. https://doi.org/10.1109/ICSE553472025.00041 [[Zha25an]](https://doi.org/10.1109/ICSE553472025.00041)

37. Qin, F., Naziri, M., Ai, H., Dutta, S., & d'Amorim, M. (2026). How Effective Is Coverage-Ged Fuzzing to Test Deep Learning Library APIs? *2026 IEEE International Conference on Software Testing, Verification and Validation (ICST)*, 88–99. https://doi.org/10.1109/ICST69053.2026.00023 [[Qin26f]](https://doi.org/10.1109/ICST69053.2026.00023)

38. Park, J., & Yun, I. (2026). Agentic Fuzzing: Opportunities and Challenges. *arXiv preprint*. https://doi.org/10.48550/arXiv.2605.10074 [[Par26d]](https://doi.org/10.48550/arXiv.2605.10074)

39. Sheng, Z., Chen, Z.-C., Xu, Q.-X., Zhu, K.-W., Huang, J. (2026). FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction. *arXiv preprint*. https://doi.org/10.48550/arXiv.2605.21779 [[She26h]](https://doi.org/10.48550/arXiv.2605.21779)

40. Zhang, Y.-T., Kang, S., Meng, R.-J., Böhme, M., & Roychoudhury, A. (2026). VeriGrey: Greybox Agent Validation. *arXiv preprint*. https://doi.org/10.48550/arXiv.2603.17639 [[Zha26cr]](https://doi.org/10.48550/arXiv.2603.17639)

41. Mao, X., Qian, R., Zheng, X., & Wang, C. (2026). Agent Hacks Agents: Autoresearch Discovers Vulnerabilities in Production Agents. *arXiv preprint*. https://arxiv.org/abs/2607.11698 [[Mao26d]](https://arxiv.org/abs/2607.11698)

42. Jahan, S., Shah, M. B., Mahbub, P., & Rahman, M. M. (2025). Improved Detection and Diagnosis of Faults in Deep Neural Networks Using Hierarchical and Explainable Classification. *2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)*, 2944–2956. https://doi.org/10.1109/ICSE553472025.00224 [[Jah25]](https://doi.org/10.1109/ICSE553472025.00224)

43. Wang, X., Chen, Y., Li, J.-C., Wang, Y.-X., Yao, Y., Gu, T.-L., ... & Hu, X. (2026). OpenRT: An Open-Source Red Teaming Framework for Multimodal LLMs. *arXiv preprint*. https://doi.org/10.48550/arXiv.2601.01592 [[Wan26cc]](https://doi.org/10.48550/arXiv/2601.01592)

44. Chen, Z.-R., Liu, X., Kang, M., Zhang, J., Pan, M.-Z., Yang, S., & Li, B. (2025). ARMs: Adaptive Red-Teaming Agent against Multimodal Models with Plug-and-Play Attacks. *arXiv preprint*. https://doi.org/10.48550/arXiv.2510.02677 [[Che25ad]](https://doi.org/10.48550/arXiv.2510.02677)

45. Lyu, Y., Chen, P., Wu, F., Yu, J., Hon, K.-L., & Chen, H. (2026). FuzzAgent: Multi-Agent System for Evolutionary Library Fuzzing. *arXiv preprint*. https://doi.org/10.48550/arXiv.2605.14431 [[Lyu26c]](https://doi.org/10.48550/arXiv.2605.14431)

46. Jahan, S., Rajput, S., Sharma, T., & Rahman, M. M. (2026). Hierarchical Fault Detection and Diagnosis for Transformer Architectures. *arXiv preprint*. https://arxiv.org/abs/2604.28118 [[Jah26b]](https://arxiv.org/abs/2604.28118)

47. He, P.-F., Miculicich, L., Sharma, V., Fox, A., Lee, G., Tang, J.-L., ... & Le, L. T. (2026). PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections. *arXiv preprint*. https://doi.org/10.48550/arXiv.2606.12737 [[He26o]](https://doi.org/10.48550/arXiv.2606.12737)

---

**报告生成日期**: 2026年10月24日
**文献检索平台**: Undermind AI
**分析工具**: ARS-Codex academic-research-suite
**BibTeX文件**: C:\Users\25636\研究方向_相关文献_2025-2026.bib
